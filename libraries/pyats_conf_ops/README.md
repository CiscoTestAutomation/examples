## demo8_pyats_conf_ops

# Introduction

This script carries the knowledge of demo6. This time, it is uses within a
pyATS script. This script is a pyATS scripts, which uses those objects to
configuration and make sure the devices are configured correctly. This script
works on all platform.

This scripts requires the device to not be configured, as the configuration
is done by the script. Make sure you are using the unconfigured virl devices.

# Execution

This demo requires devices. There is 2 options on how to run this demo:

1) This demo is ready to be used with the VIRL devices. Please follow the guide
   <here> on how to boot the virtual devices. Make sure to use the VIRL file which
   does not configure both devices as the configuration is done within the script.

2) Use your own devices. Please modify the testbed file with the devices'
   names and the corresponding IP addresses.

```
pyats run job job/demo8_pyats_conf_ops_job.py --testbed-file virl.yaml --datafile datafile.yaml
```

# Output

The log can be viewed in the file `logviewer`.
