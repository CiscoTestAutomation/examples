## demo10_robot

# Introduction

`RobotFramework` is an opensource test automation framework which provides automation,
without having to write code. It is `Keyword` driven. Libraries provide
Keywords to interact. `Genie` and `pyATS` provide keywords, to execute
Triggers and Testcases, parse commands, learn device features and many more.  It also uses
`Genie` `Operational` object, to verify if we have a right amount of Routes, up
interfaces, etc. 

This demo is an advance version of Demo 5.

# Execution

This demo requires devices. There is 3 options on how to run this demo:

Make sure you have robotframework installed
```
pip install robotframework
```

1) Use mock devices. We have used the Unicon playback feature to record all
   interactions with the device so you can use it smoothly without connecting
   to real devices as below.

```
export unicon_replay=mock_device
robot demo10_nxos.robot
```

2) This demo is ready to be used with the VIRL devices. Please follow the guide
   <here> on how to boot the virtual devices.

3) Use your own devices. Please modify the testbed file with the devices'
   names and the corresponding IP addresses.

```
<open the demo10_nxos.robot file, and modify the testbed variable to point to your testbed file>
robot demo10_nxos.robot
```

** demo10_iosxr.robot & demo10_iosxe.robot can be run the same way **

# Output

The log can be viewed in the log.html