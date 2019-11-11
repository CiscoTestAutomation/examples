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
    chosen_uut_device = 'VM-4'
    stdby_device = 'notreallyadevice'
    if_name = 'mgmt0'
    mtu = 1500

    #
    #NOTE: Not all fields in "show interface mgmt0" can be parsed by parsergen
    #      nontabular parser in a single pass.  
    #      The line "x broadcast packets Y bytes" is 
    #      identical in both the "Rx" and "Tx" sections, this is a known 
    #      limitation and has been documented.
    #
    #      In this case, this limitation can be worked around as follows:
    #      - First, the section titles "Rx" and "Tx" would have to be given
    #        their own regex tags and parsed along with other fields.  This
    #        gives parsergen a hook into the particular sections of interest.
    #
    #      - Then, a first-pass parse would be done to get all the fields
    #        except the fields in the "Rx" and "Tx" section.  Note that this
    #        would only work for a command such as "show interface mgmt0"
    #        and would not work for a command such as "show interface"
    #        because parsergen would not know where to hook into the output
    #        (multiple interfaces, multiple sections Rx/Tx per interface).
    #
    #      - Then, a second-pass parse would be done by explicitly specifying
    #        the "Rx" section in oper_fill (to hook into this section). The
    #        user would then assign the generic fields just parsed to 
    #        section-specific fields.
    #
    #      - Then, a third-pass parse would be done similarly against the
    #        "Tx" section.
    #

    show_arp_header_fields= [ "Address",
                              "Age",
                              "MAC Address",
                              "Interface" ]
    show_arp_table_parse_index = [0, 3]
    show_arp_table_title_pattern = None


    run(testscript=test_path + '/parsergen_demo.py',
        uut_name=chosen_uut_device,
        stdby_name=stdby_device, if_name=if_name, mtu=mtu, 
        show_arp_header_fields=show_arp_header_fields, 
        show_arp_table_parse_index=show_arp_table_parse_index,
        show_arp_table_title_pattern=show_arp_table_title_pattern)
