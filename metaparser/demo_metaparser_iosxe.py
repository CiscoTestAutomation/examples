#
# imports
#
import pprint
import argparse

from ats.topology import loader
from genie.libs.parser.iosxe.show_interface import ShowInterfaces


def load(testbed, device_name):
    tb = loader.load(testbed)
    try:
        return tb.devices[device_name]
    except KeyError as e:
        raise KeyError("Could not find '{d}' within "
                       "testbed '{tb}'".format(d=device, tb=testbed))

def parse(device):
    return ShowInterfaces(device).parse()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arguments for '
                                                 'demo8_metaparser')
    parser.add_argument('-testbed_file',
                        help='Location of the testbed file',
                        default = 'virl.yaml')

    parser.add_argument('-device',
                        help='Name or alias of the device to parse on',
                        default = 'helper')

    custom_args = parser.parse_known_args()[0]
    testbed_file = custom_args.testbed_file
    device_name = custom_args.device

    device = load(testbed_file, device_name)
    device.connect()

    parsed = parse(device)
    pprint.pprint(parsed)
