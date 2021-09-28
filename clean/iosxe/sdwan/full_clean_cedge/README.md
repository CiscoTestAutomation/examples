## pyATS Clean for IOSXE SDWAN (cEdge) devices

This folder contains the following sample files:

- clean.yaml file for IOSXE SDWAN (cEdge) devices
- testbed.yaml file for IOSXE SDWAN (cEdge) devices

These files can be used as a template to execute a full end-to-end clean on IOSXE SDWAN (cEdge) It performs the following steps in order:

- connects to IOSXE SDWAN devices
- let device goes into ROMMON mode and boot from ROMMON as autonomous mode
- apply bootstrap configuration for image copy
- (Optional) pings execution servers to verify connectivity
- copies images to device
- expand .bin image as install mode
- change mode to controller mode from autonomous mode and reload
- apply bootstrap configuration

If the devices are not in stable state at the time of execution, pyATS Clean
provides a built-in recovery mechanism, where it attempts to bring the device
back to stable state by powercycling the device and then rebooting it from
rommon with a known stable (golden) image.

Please substitute your device IP addresses, credentials and image directories in the templates provided before use.
