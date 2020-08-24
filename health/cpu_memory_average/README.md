## pyATS Health for cpu/memory average check

This folder contains following pyATS health yaml file:

- health_cpu_memory_average.yaml

The file can be used as a template to monitor/check a cpu load and memory usage on devices.

Please adjust some parameters such as device, threshold and etc to your testbed/job before use.

### How to use

```
pyats run job <job file> --health-file health_cpu_memory_average.yaml
```