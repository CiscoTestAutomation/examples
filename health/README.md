# pyATS Health Examples

This repository contains usage examples for the pyATS Health library. These are
not working examples, but rather:

- showcase **the various features and functionalities** of the pyATS health

- demonstrate **how to use the pyATS Health libraries**

pyATS Health leverages Quick Trigger (Blitz) YAML format. So, can develop what you want to monitor and collect with Blitz and easily migrate from `Blitz` to `pyATS Health`.

The usecases and examples provided in this repository can be tried with your pyATS job.
But some of parameters such as device, threshold and etc might need to be adjusted for your env/job.

## Getting Started

```bash

# 1. make sure pyATS is installed (including the libraries)
bash$ pip install pyats[full]

# Cisco Internal only
bash$ pip install ats[full]

# 2. ensure the pyATS clean library is installed
bash$ pip list | grep genie.libs.health

# 3. clone this repository into your environment
bash$ git clone https://github.com/CiscoTestAutomation/examples

```

## General Information

- pyATS Clean Documentation: https://pubhub.devnetcloud.com/media/genie-docs/docs/health/index.html
- Website: https://developer.cisco.com/pyats/
- Documentation: https://developer.cisco.com/docs/pyats/
- Support: pyats-support-ext@cisco.com


# Contribution

Feel free to open PR against this repository for any example of pyATS health emal, any enhancements or bug fixes you wish to add.