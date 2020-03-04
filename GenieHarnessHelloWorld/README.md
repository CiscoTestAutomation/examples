# Genie Harness Hello World!

The Trigger datafile

1. cd $VIRTUAL_ENV
2. git clone git@github.com:CiscoTestAutomation/examples.git
3. cd examples/GenieHarnessHelloWorld
4. export PYTHONPATH=$VIRTUAL_ENV
5. pyats run genie --trigger-uids HelloWorld --trigger-datafile trigger_datafile.yaml --subsection-datafile subsection_datafile.yaml --testbed-file testbed.yaml

Step 4 is to simplify the python path. 
