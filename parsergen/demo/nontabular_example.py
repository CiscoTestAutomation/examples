#
# imports
#
import pprint
import argparse

from ats.topology import loader

from genie import parsergen
import nontabular_markup


def load(testbed, device_name):
    tb = loader.load(testbed)
    try:
        return tb.devices[device_name]
    except KeyError as e:
        raise KeyError("Could not find '{d}' within "
                       "testbed '{tb}'".format(d=device, tb=testbed))

def parse_cli(device):
    output = device.execute('show interface brief')

    attrValPairsToParse = [
        ('show.intf.if_name', 'mgmt0'),
    ]

    pgfill = parsergen.oper_fill (
        device,
        ('show_interface_<WORD>', [], {'ifname':'mgmt0'}),
        attrValPairsToParse,
        refresh_cache=True, regex_tag_fill_pattern='show\.intf')

    result = pgfill.parse()
    return parsergen.ext_dictio[device.name]
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arguments for '
                                                 'demo10_parsergen')
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
    pprint.pprint(cli_parsed)
