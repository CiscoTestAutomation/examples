## demo2_harness_triggers

# Introduction

This script demonstrates the Triggers and Verifications concept in Genie.
Triggers and verifications are plug and play Testcase to create any combination
of tests.

The list of triggers and verifications can be found here: 

* Connect to the devices defined in the testbed file.
* Execute the first round of `verifications`. These verifications take a snapshot
  of the state of these commands. Future round of verifications is compared with
  these initial snapshot.
* Execute the first trigger `TriggerClearCountersInterfaceAll`.
* Execute the second round of verifications. Those are compared with the first round.
* Execute the second trigger `TriggerShutNoShutBgpNeighbors`.
* Repeat until all triggers are executed.
* Terminate the run

# Execution

This demo requires devices. There is 3 options on how to run this demo:

1) Use mock devices. We have used the Unicon playback feature to record all
   interactions with the device so you can use it smoothly without connecting
   to real devices as below.

```
pyats run job demo2_harness_triggers_job.py --testbed-file cisco_live.yaml --replay mock_device
```

2) This demo is ready to be used with the VIRL devices. Please follow the guide
   <here> on how to boot the virtual devices.

3) Use your own devices. Please modify the testbed file with the devices'
   names and the corresponding IP addresses.

```
pyats run job demo2_harness_triggers_job.py --testbed-file virl.yaml
```

# Output

The log can be viewed in the file `TaskLog.html`.

# What's next?

Move on to the next demo `demo3_harness_telemetry` to add healthcheck
capabilities to your testing!
