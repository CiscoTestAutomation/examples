## demo7_trigger_within_pyats

# Introduction

This script demonstrates how to include `Genie` Triggers and Verifications
within any existing `pyATS` script.

Make sure to read https://pubhub.devnetcloud.com/media/pyats-packages/docs/genie/userguide/harness/user/pyats.html for more details!

# Execution

This demo requires devices. There is 3 options on how to run this demo:

1) Use mock devices. We have used the Unicon playback feature to record all
   interactions with the device so you can use it smoothly without connecting
   to real devices as below.

```
pyats run job job/demo7_trigger_within_pyats_job.py --testbed-file cisco_live.yaml --replay mock_device
```

2) This demo is ready to be used with the VIRL devices. Please follow the guide
   <here> on how to boot the virtual devices.

3) Use your own devices. Please modify the testbed file with the devices'
   names and the corresponding IP addresses.

```
pyats run job job/demo7_trigger_within_pyats_job.py --testbed-file virl.yaml
```

# Output

The log can be viewed in the file `TaskLog.html`.

# What's next?

Go ahead and add to your existing pyATS script any Genie Triggers for better coverage!
