## pyATS Clean for NXOS N9K Hardware

This folder contains the following sample files:

- clean.yaml file for NXOS N9K Hardware platform
- testbed.yaml file for NXOS N9K Hardware platform

These files can be used as a template to execute a full end-to-end clean on an
NXOS N9K device. It performs the following steps in order:

- connects to NXOS N9K Hardware device
- (Optional) pings execution servers to verify connectivity
- (Optional) copies necessary images to intermediate server
- copies images to device
- changes boot variables
- executes 'write erase'
- reload device
- apply base configuration after reload
- verifies the running image matches what was specified
