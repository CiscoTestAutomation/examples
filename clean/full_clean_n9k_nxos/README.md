## pyATS Clean for NXOS N9K Hardware

This folder contains the following sample files:

- clean.yaml file for NXOS N9K hardware platform
- testbed.yaml file for NXOS N9K hardware platform

These files can be used as a template to execute a full end-to-end clean on an
NXOS N9K hardware device. It performs the following steps in order:

- connects to NXOS N9K hardware device
- (Optional) pings execution servers to verify connectivity
- (Optional) copies necessary images to intermediate server
- copies images to device
- changes boot variables
- executes 'write erase'
- reload device
- apply base configuration after reload
- verifies the running image matches what was specified

If the devices are not in stable state at the time of execution, pyATS Clean
provides a built-in recovery mechanism, where it attempts to bring the device
back to stable state by powercycling the device and then rebooting it from
rommon with a known stable (golden) image.

Please substitute your device IP addresses, credentials and image directories in
the templates provided before use.
