#
# imports
#
import argparse

from genie.conf import Genie
from genie.libs import conf, ops
from genie.abstract import Lookup


def load(testbed, devices_name):
    tb = Genie.init(testbed)
    ret = []
    for device in devices_name:
        try:
            ret.append(tb.devices[device])
        except KeyError as e:
            raise KeyError("Could not find '{d}' within "
                           "testbed '{tb}'".format(d=device, tb=testbed))
    return ret

def configure_ospf(device, router_id_digit, unconfig=False):
    lookup = Lookup.from_device(device, packages={'conf':conf, 'ops':ops})
    ospf = conf.ospf.ospf.Ospf()
    ospf.device_attr[device].vrf_attr['default'].instance = '9'
    ospf.device_attr[device].vrf_attr['default'].router_id = '9.9.9.{}'.format(\
                                                                router_id_digit)
    device.add_feature(ospf)

    if unconfig:
        print('Removing configuration for {d}'.format(d=device))
        ospf.build_unconfig()
    else:
        print('Applying configuration for {d}'.format(d=device))
        ospf.build_config()

def retrieve_ospf(device):
    lookup = Lookup.from_device(device)
    ospf = lookup.ops.ospf.ospf.Ospf(device)
    ospf.learn()

    # Compare of take a snapshot
    if hasattr(device, 'snapshot'):
        diff = ospf.diff(device.snapshot, exclude=['age', 'dead_timer',
                                                   'hello_timer'])
        if diff:
            print('Found some difference for device {d}'.format(d=device))
            print(diff)
    else:
        device.snapshot = ospf


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arguments for '
                                                 'demo12_conf_ops')
    parser.add_argument('-testbed_file',
                        help='Location of the testbed file',
                        default = 'virl.yaml')

    parser.add_argument('-devices',
                        help='Names or alias of the device to configure and '
                             'retrieve the operational state',
                        default = 'uut helper')

    custom_args = parser.parse_known_args()[0]
    testbed_file = custom_args.testbed_file
    devices_name = custom_args.devices.split(' ')

    devices = load(testbed_file, devices_name)
    router_id_digit = 0

    # Connect to devices
    for device in devices:
        device.connect()
        device.mapping = {}

    # Take initial snapshot of Ospf - Will be used for comparison later
    # On both devices
    for device in devices:
        retrieve_ospf(device)

    # Config Ospf on both devices
    for device in devices:
        router_id_digit += 1
        configure_ospf(device, router_id_digit)

    # Take new snapshot and compare with initial snapshot
    for device in devices:
        retrieve_ospf(device)

    # Remove Ospf configuration that we added
    for device in devices:
        configure_ospf(device, router_id_digit, unconfig=True)
