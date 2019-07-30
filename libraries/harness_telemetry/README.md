## demo3_harness_telemetry

# Introduction

This script demonstrates the Triggers and Verifications with Healthcheck.
The Healthcheck is called `Genie Telemetry`. It allows to collect any kind of
information in the execution, act on it and create a report at
the end of the run. For example, verify if any core was created
after each trigger, verify cpu usage, traceback, etc.

The execution flow will be the same as demo2_harness_triggers, with the
following addition:

* At the end of CommonSetup, all Triggers and at the begining of CommonCleanup,
  it is verified if there is any core on the device and any traceback.

# Execution

This demo requires devices. There is 3 options on how to run this demo:

1) Use mock devices. We have used the Unicon playback feature to record all
   interactions with the device so you can use it smoothly without connecting
   to real devices as below.

```
pyats run job demo3_harness_telemetry_job.py --testbed-file cisco_live.yaml --replay mock_device
```

2) This demo is ready to be used with the VIRL devices. Please follow the guide
   <here> on how to boot the virtual devices.

3) Use your own devices. Please modify the testbed file with the devices'
   names and the corresponding IP addresses.

```
pyats run job demo3_harness_telemetry_job.py --testbed-file virl.yaml --genietelemetry telemetry.yaml
```

# Output

The log can be viewed in the file `TaskLog.html`.

# What's next?

Move on to the next demo `demo4_harness_custom_trigger` to add your own
Triggers!
