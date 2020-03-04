# Genie Harness Hello World!

The Trigger datafile contains the Testcase information.
 * Whats the name of the testcase
 * Where is it situated (Python path)
 * On which device to execute this trigger.

## Steps to execute this Hello World:

1. cd $VIRTUAL_ENV
2. git clone git@github.com:CiscoTestAutomation/examples.git
3. cd examples/GenieHarnessHelloWorld
4. export PYTHONPATH=$VIRTUAL_ENV
5. pyats run genie --trigger-uids HelloWorld --trigger-datafile trigger_datafile.yaml --subsection-datafile subsection_datafile.yaml --testbed-file testbed.yaml
6. pyats logs view

Step 4 is to simplify the python path. 

In Step 5 we need to provide the following:

* What Testcase to execute with trigger-uids, multiple testcase can be provided
* Where is the yaml file which contains all the triggers definition
* Where is the subsection datafile, customize what to execute before/after the testcases
* The testbed file

The actual testcase is held within the file `HelloWorld.py`. This is where the testcase and action to the device reside.

## More Advance testcase

1. pyats run genie --trigger-uids "HelloWorld Basic" --trigger-datafile trigger_datafile.yaml --subsection-datafile subsection_datafile.yaml --testbed-file testbed.yaml
2. pyats logs view

With the harness, you write many tests and you select what to execute. In this
case, we selected `HelloWorld` and `Basic`.

In the `Basic` testcase, we sent commands to the device. There are many different API to use to interact with the devices; here are the most useful ones.

1. device.parse('show version') <-- Call a parser and returns a dictionary datastructure
2. device.execute('show version') <-- Send command to the device and return string from the device
3. device.configure('interface ethernet2/2\nshutdown') <-- Go to conf t and send configuration to th    e device
4. device.api.get_interface_mtu_size('Ethernet2/2') <-- Call any of our apis
5. device.learn('bgp') <-- OS Agnostic model for specific feature. The object returned has a .info which gives a dictionary which is identical between all OS.

The full list of available parsers, learn and api is available here: https://pubhub.devnetcloud.com/media/genie-feature-browser/docs/#/
