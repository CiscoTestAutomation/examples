# Description: This example connects to a previous set-up XRVR router,
#              executes some show commands and parses via cAAs/TCL and
#              parsergen/Python, with differences in the parse results
#              shown.

import os
from ats.easypy import run

def main():
    # Find the examples/tests directory where the test script exists
    test_path = (os.path.dirname(os.path.abspath(__file__)))
    # Do some logic here to determine which devices to use
    # and pass these device names as script arguments
    # ...
    chosen_uut_device = 'ASIM2'
    stdby_device = 'notreallyadevice'
    if_name = 'management'
    mtu = 1500


    show_arp_header_fields= [ "IP address",
                              "HW type",
                              "Flags",
                              "HW address",
                              "Mask",
                              "Device" ]
    show_arp_table_parse_index = [0, 5]
    show_arp_table_title_pattern = None


    run(testscript=test_path + '/parsergen_demo_aireos.py',
        uut_name=chosen_uut_device,
        stdby_name=stdby_device, if_name=if_name,
        show_arp_header_fields=show_arp_header_fields,
        show_arp_table_parse_index=show_arp_table_parse_index,
        show_arp_table_title_pattern=show_arp_table_title_pattern)
