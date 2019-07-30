## demo6_config_ops

# Introduction

Genie uses Configuration and Operational objects to drive its configuration and
operation state. The configuraiton object, `conf`, are object that once some
variable are set,  configuration is build and apply on the device. Those objects
follow Models (Ietf, openstack, Cisco Models) to make them OS agnostic.

Models are available here: <TODO>

1) Connect to a list of devices
2) Retrieve the operational state for each device
3) Apply Ospf configuration
4) Retrieve the operational state for each device and compare with step 2
5) Unconfig Ospf configuration

# Execution

This demo requires devices. There is 2 options on how to run this demo:

1) This demo is ready to be used with the VIRL devices. Please follow the guide
   <here> on how to boot the virtual devices.

2) Use your own devices. Please modify the testbed file with the devices'
   names and the corresponding IP addresses.

```
python demo6_config_ops.py --testbed-file virl.yaml
```

# Output

The log can be viewed in the file `output`.

# What's next?

Move on to the next demo `demo7_trigger_within_pyats` to learn how to run
a trigger directly from within pyATS framework.

Try Demo8, it uses all demo6 concepts into a pyATS script.
