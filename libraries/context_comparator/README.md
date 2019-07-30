## demo9_context_comparator

# Introduction

This script demonstrates how to compare show commands information between two
contexts (cli/xml). It first sends a show command with cli, then do the same
with xml, and compares the fields to make sure they are equal.

# Execution

This demo requires devices. There is 3 options on how to run this demo:

1) Use mock devices. We have used the Unicon playback feature to record all
   interactions with the device so you can use it smoothly without connecting
   to real devices as below.

```
pyats run job job/demo9_context_comparator_job.py --testbed-file cisco_live.yaml --replay mock_device
```

2) This demo is ready to be used with the VIRL devices. Please follow the guide
   <here> on how to boot the virtual devices.

3) Use your own devices. Please modify the testbed file with the devices'
   names and the corresponding IP addresses.

```
pyats run job job/demo9_context_comparator_job.py --testbed-file virl.yaml
```

# Output

The log can be viewed in the file `TaskLog.html`.
