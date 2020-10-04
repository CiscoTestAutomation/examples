```
pyats run job job.py --testbed-file ../../testbed_yamls/devnet_sandbox_always_on/testbed.yaml 

pyats run genie --testbed-file ../../testbed_yamls/devnet_sandbox_always_on/testbed.yaml --trigger-datafile blitz_config_interfaces.yaml --trigger-uids config_interface --subsection-datafile subsection_datafile.yaml --mapping-datafile mapping_datafile.yaml
