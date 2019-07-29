## demo11_harness_cluster

# Introduction

This script demonstrate how to run multiple triggers and verifications within 1
trigger; a Cluster trigger

# Execution

This demo requires devices. There is 3 options on how to run this demo:

1) Use mock devices. We have used the Unicon playback feature to record all
   interactions with the device so you can use it smoothly without connecting
   to real devices as below.

```
pyats run job demo11_harness_cluster_job.py --testbed-file cisco_live.yaml --replay mock_device
```

2) This demo is ready to be used with the VIRL devices. Follow the guide
   <here> on how to boot the virtual devices.

3) Use your own devices. Modify the testbed file with the devices'
   names and the corresponding IP addresses.

```
pyats run job demo11_harness_cluster_job.py --testbed-file virl.yaml
```

# Output

The log can be viewed in the file `TaskLog.html`.

