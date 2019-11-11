Description:
------------
This README file is located in examples/parsergen/pyAts.

These sample pyATS jobs log into a router you specify on a testbed that you
specify, runs "show interface" and parses the output using cAAS/TCL and
re-runs the command and this time parses the output using parsergen/Python.

A comparison between the parsed results is then done, with results shown
in the log.

A parsergen comparison test is then run, where only user-selected parts of
the output are parsed and compared to expected values.

A show command producing tabular output is then run, and outputs parsed.

Either csccon or unicon connection providers are supported.

The following demo jobs are provided on various reference platforms:

parsergen_demo_vios_job.py
parsergen_demo_viosxe_job.py
parsergen_demo_vnxos_job.py
parsergen_demo_xrvr_job.py
parsergen_demo_aireos_job.py
parsergen_demo_enxr_job.py

The following jobs invoke tests that use non-default connection aliases:

parsergen_demo_aireos_job_conn_alias.py
parsergen_demo_enxr_job_conn_alias.py


To launch this sample pyATS job:
--------------------------------

1. Pick a testbed to run the job against and identify the YAML file

2. Substitute in parsergen_demo_job.py your UUT name, as per your YAML file,
   as chosen_uut_device.

3. Launch the job.
easypy parsergen_demo_<plat>_job.py -testbed_file /path/to/your_testbed.yaml


To launch the EnXR sample pyATS job:
------------------------------------

1. pip install dyntopo

2. cd examples

3. easypy parsergen/pyAts/parsergen_demo_enxr_job.py -logical_testbed_file dyntopo_xrut/yaml/ios_enxr_ping_test_config.yaml -clean_file dyntopo_xrut/yaml/ios_enxr_ping_bringup_config.yaml

