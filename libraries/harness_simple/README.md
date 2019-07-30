## demo1_harness_simple

# Introduction

This script is an introduction to `Genie`. It does the following:

* Connect to the devices defined in the testbed file.
* Execute a Sleep Trigger. Will sleep for 5 seconds. This time can be modified
  in the Triggerdatafile (Location provided in the job file).
* Terminate the run

# Execution

This demo requires devices. There is 3 options on how to run this demo:

1) Use mock devices. We have used the Unicon playback feature to record all
   interactions with the device so you can use it smoothly without connecting
   to real devices as below.

```
pyats run job demo1_harness_simple_job.py --testbed-file cisco_live.yaml --replay mock_device
```

2) This demo is ready to be used with the VIRL devices. Please follow the guide
   <here> on how to boot the virtual devices.

3) Use your own devices. Please modify the testbed file with the devices'
   names and the corresponding IP addresses.

```
pyats run job demo1_harness_simple_job.py --testbed-file virl.yaml
```

# Output

The log can be viewed in the file `TaskLog.html`.

# What's next?

Move on to the next demo `demo2_harness_triggers` to add useful `Triggers` and
`Verifications` to your testing!
