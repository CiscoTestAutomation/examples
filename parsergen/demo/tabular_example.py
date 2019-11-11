#
# imports
#
import pprint
import argparse

from genie import parsergen
from ats.topology import loader


def load(testbed, device_name):
    tb = loader.load(testbed)
    try:
        return tb.devices[device_name]
    except KeyError as e:
        raise KeyError("Could not find '{d}' within "
                       "testbed '{tb}'".format(d=device, tb=testbed))

def parse_cli(device):
    # By the default it will take cli
    output = device.execute('show interface brief')
    result = parsergen.oper_fill_tabular(
            device_output= output,
            device_os= 'nxos',
            header_fields= [['Ethernet', 'VLAN', 'Type', 'Mode', 'Status', 'Reason', 'Speed', 'Port'],
                            ['Interface', '', '', '', '', '', '', 'Ch \#']],
            label_fields=['Ethernet Interface', 'VLAN', 'Type',
                          'Mode', 'Status', 'Reason', 'Speed', 'Port'],
            index= [0])

    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arguments for '
                                                 'demo_parsergen')
    parser.add_argument('-testbed_file',
                        help='Location of the testbed file',
                        default = 'virl.yaml')

    parser.add_argument('-device',
                        help='Name or alias of the device to parse on',
                        default = 'uut')

    custom_args = parser.parse_known_args()[0]
    testbed_file = custom_args.testbed_file
    device_name = custom_args.device

    device = load(testbed_file, device_name)
    device.connect()

    cli_parsed = parse_cli(device)
    pprint.pprint(cli_parsed.entries)
