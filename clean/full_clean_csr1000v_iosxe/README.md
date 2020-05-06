## pyATS Clean for IOSXE CSR1000v

This folder contains the following sample files:

- clean.yaml file for IOSXE CSR1000v platform
- testbed.yaml file for IOSXE CSR1000v platform

These files can be used as a template to execute a full end-to-end clean on an
IOSXE CSR1000v device. It performs the following steps in order:

- connects to IOSXE CSR1000v device
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
