# Genie Harness Hello World!

The Trigger datafile contains the Testcase information.
 * Whats the name of the testcase
 * Where is it situated (Python path)
 * On which device to execute this trigger.

Steps execute this Hello World

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
