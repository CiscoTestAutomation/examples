## pyATS Health for cpu/memory custom check

This folder contains following pyATS health yaml file:

- health_cpu_memory_custom.yaml

The file can be used as a template to create custom pyATS Health Check.
In this example, having monitor/check a cpu load and memory usage on devices in health yaml.

Please adjust some parameters such as device, threshold and etc to your testbed/job before use.

### How to use

```
pyats run job ../../blitz/config_interface/job.py --testbed-file ../../blitz/config_interface/testbed.yaml --health-file health_cpu_memory_custom.yaml
```