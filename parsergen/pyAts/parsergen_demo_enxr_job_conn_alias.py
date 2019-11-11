#
# Description: This example brings up a previously built EnXR router,
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
    chosen_uut_device = 'r1'
    stdby_device = 'notreallyadevice'
    if_name = 'GigabitEthernet0/2/0/0'
    mtu = 1514
    header_fields= [ "Address",
                      "Age",
                      "Hardware Addr",
                      "State",
                      "Type",
                      "Interface" ]
    show_arp_table_parse_index = [0, 5]
    show_arp_table_title_pattern = r"^(\d+/\d+/CPU\d+)"


    run(testscript=test_path + '/parsergen_demo_conn_alias.py',
        uut_name=chosen_uut_device,
        stdby_name=stdby_device, if_name=if_name, mtu=mtu,
        show_arp_header_fields=header_fields,
        show_arp_table_parse_index=show_arp_table_parse_index,
        show_arp_table_title_pattern=show_arp_table_title_pattern)
