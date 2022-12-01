
## Blitz Configure Interface Description

This folder contains following blitz file

- blitz.yaml (trigger_datafile with Blitz style)

What this Blitz yaml does is:
- access to R1_xe (iosxe) device
- default interface on both Gi2 and Gi3
- configure interface description `configure by pyATS` on both Gi2 and Gi3
- check the interface description is configured as expected

### How to use:
```
pyats run job job.py --testbed-file testbed.yaml 
```
