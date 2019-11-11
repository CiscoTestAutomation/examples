#
# imports
#
import pprint
import argparse

from ats.topology import loader
from genie.libs.parser.nxos.show_bgp import ShowBgpProcessVrfAll


def load(testbed, device_name):
    tb = loader.load(testbed)
    try:
        return tb.devices[device_name]
    except KeyError as e:
        raise KeyError("Could not find '{d}' within "
                       "testbed '{tb}'".format(d=device, tb=testbed))

def parse_cli(device):
    # By the default it will take cli
    return ShowBgpProcessVrfAll(device).parse()

def parse_xml(device):
    return ShowBgpProcessVrfAll(device, context=['xml']).parse()

def parse_xml_cli(device):
    # Parse Xml, and if any key is missing, complete it with cli output
    return ShowBgpProcessVrfAll(device, context=['xml', 'cli']).parse()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Arguments for '
                                                 'demo8_metaparser')
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

    xml_parsed = parse_xml(device)
    pprint.pprint(xml_parsed)

    xml_cli_parsed = parse_xml_cli(device)
    pprint.pprint(xml_cli_parsed)
