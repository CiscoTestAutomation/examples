# Hierarchical loops and retry scopes

This example requires a pyATS installation that supports stacked loop and retry
decorators. It runs locally without a testbed or network devices.

From the repository root, run the Easypy job:

```bash
pyats run job loop_retry/example_job.py
```

Or run the AEtest script directly:

```bash
python loop_retry/example_script.py
```

`HierarchicalLoops` runs the depth-first Cartesian product:

```text
west router1
west router2
east router1
east router2
```

Its generated section UIDs use adjacent parameter brackets, for example
`check_device[region=west][device=router1]`. `CustomLoopUIDs` supplies explicit
UIDs instead: `west/router1` and `west/router2`. Explicit UIDs replace the
generated section prefix for their dimension.

The remaining testcases deliberately fail `west/router1` on its first attempt.
Each allows one retry with no wait. The decorator placement controls its scope:

| Testcase | Retry position | Invocations |
| --- | --- | --- |
| `RetryWholeLoop` | Outside both loops | All four combinations, then all four again: 8 total. |
| `RetryPerRegion` | Between the loops | Both west devices twice, then both east devices once: 6 total. |
| `RetryPerDevice` | Inside both loops | West/router1 twice, then each other combination once: 5 total. |

Retry UIDs gain ` [Retry 1]`. All attempts remain visible in the report, while
superseded attempts are excluded from the final summary. The three retry
testcases finish with `PASSX`, indicating recovery after the intentional
failure. `retry_count` is the attempt index for the active retry boundary;
the east region starts at zero in `RetryPerRegion`.

See the [loop documentation](https://github.com/CiscoTestAutomation/pyats/blob/main/docs/aetest/loop.rst)
and [retry documentation](https://github.com/CiscoTestAutomation/pyats/blob/main/docs/aetest/retry.rst)
for configuration, filtering and custom generator behavior.
