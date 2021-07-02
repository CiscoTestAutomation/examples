## pyATS Health for cpu/memory average check

This folder contains no yaml file. pyATS Health Check has pre-defined checks for `cpu`, `memory`, `logging` and `core`.

But of course, you need to have pyATS job where you want to run pyATS Health Check. So, we will use Blitz example (config_interface) here.

[blitz/config_interface](https://github.com/CiscoTestAutomation/examples/tree/master/blitz/config_interface)

Please find the detail what the Blitz does from above example.

### How to use:
```
pyats run job ../../blitz/config_interface/job.py --testbed-file ../../blitz/config_interface/testbed.yaml --health-checks cpu memory logging core --replay mock_device
```
NOTE: above use `--replay` (mock device). so you don't need to have device to run.

As you can see above, what you need to do is just adding health check names such as `cpu`, `memory`, `logging` and `core`. These checks will run as post processor per testcase.

Here are some information about what each check does:

| health check | description |
|--------------|-------------|
| cpu          | cpu load check. check total of cpu load with threshold 90% by default. |
| memory       | memory usage check. check total of memory usage with threshold 90% by default. |
| logging      | keyword check in show logging output. default keywords are traceback, Traceback, TRACEBACK |
| core         | check if core file is generated on device. just check by default. Please use `--health-remote-device` to copy the core file to remote server. |


