#!/bin/env python
###################################################################
# connection_example.py : A test script example which includes:
#     common_seup section - device connection, configuration
#     Tescase section with testcase setup and teardown (cleanup)
#     subtestcase section with subtestcase setup and teardown (cleanup)
#     common_cleanup section - device cleanup
# The purpose of this sample test script is to show how to connect the
# devices/UUT in the common setup section. How to run few simple testcases
# (testcase might contain subtests).And finally, recover the test units in
# the common cleanup section.
###################################################################

import re
import pprint
import logging
from genie import parsergen as pg

from ats import aetest
from ats.log.utils import banner
from genie.parsergen.examples.parsergen.pyAts import parsergen_demo_mkpg
from csccon.expect import exp_internal

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

parameters = {}


###################################################################
###                  COMMON SETUP SECTION                       ###
###################################################################

# Configure and setup all devices and test equipment in this section.
# This should represent the BASE CONFIGURATION that is applicable
# for the bunch of test cases that would follow.

class common_setup(aetest.CommonSetup):
    """ Common Setup for Sample Test """
    @aetest.subsection
    def connect(self, testbed, uut_name):
        """ common setup subsection: connecting devices """

        log.info(banner("aetest common setup connection to device"))

        # Step 1
        self.parameters['testStep'] = 1
        log.info(banner("STEP %s: Device Connection" %
                                (self.parameters['testStep'])))

        # Get the names of devices (uut and stdby)

        # Grab the device object of the uut device with that name
        uut = testbed.devices[uut_name]
        # Save it in parameters to be able to use it from other test sections
        parameters['uut'] = uut

        # Connect to the device
        uut.connect()


        # Make sure that the connection went fine
        if not hasattr(uut, 'execute'):
            self.failed()

        if uut.execute !=  uut.connectionmgr.default.execute:
            self.failed()

        log.info ("STEP %s: Device Connection Passed" %
                  (self.parameters['testStep']))

    @aetest.subsection
    def show_exec(self, uut):
        """ common setup subsection: exec show command """
        self.parameters['testStep'] += 1
        log.info(banner("STEP %s: Device Execution Show CMD" %
                      (self.parameters['testStep'])))

        log.info ("show time")
        # Sending show clock to the device as an execute cmd
        output = uut.execute('show time')
        # Make sure the output is not none
        if output is not None:
            log.info ("The outputs is: %s" % (output))
            log.info \
            ("STEP %s: Device Execution Show CMD Passed" %
                        (self.parameters['testStep']))
        else:
            self.failed()

#######################################################################
###                          TESTCASE BLOCK                         ###
#######################################################################
#
# Place your code that implements the test steps for the test case.
# Each test may or may not contains sections:
#           setup   - test preparation
#           test    - test action
#           cleanup - test wrap-up

class tc_one(aetest.Testcase):
    """This test case parses the same output with parsergen"""
    @aetest.setup
    def tc_one_setup(self):
        """ test setup """
        log.info("Pass testcase setup")


    @aetest.test
    def pythonNonTabularParsing(self, uut, if_name):
        """ Native Python Parsing """


        device = uut

        # Mark desired keys with "None"
        # Due to two
        # Overly similar router output (STATE....) is shared among
        # multiple lines, this makes most of the keys inaccessible to
        # parsergen and makes it impossible to use the
        # regex_tag_fill_pattern convenience feature.
        # Grab what keys we can for the purposes of the demonstration.
        attrValPairsToParse = [
            ('show.intf.if_name',                 if_name),
            ('show.intf.mac_address',             None),
            ('show.intf.ip_address',              None),
            ('show.intf.ip_gateway',              None),
            ('show.intf.ip_prefix',               None),
            ('show.intf.ext_nat_ip_state',        None),
            ('show.intf.ext_nat_ip_address',      None),
            ('show.intf.link_local_ipv6_address', None),
        ]
        pgfill = pg.oper_fill (
            uut,
            ('show_interface_<WORD>', [], {'ifname':if_name}),
            attrValPairsToParse,
            refresh_cache=True)
        result = pgfill.parse()
        log.info("Parsing result : {}".format(result))
        if result:
            parseresult_python = pg.ext_dictio[uut.name]
            log.info("Parsing details : {}".format(parseresult_python))
        else:
            log.error(str(pgfill))


        attrValPairsToCheck = [
            ('show.intf.if_name',              if_name),
            ('show.intf.link_local_if_state',  'REACHABLE'),
        ]

        pgcheck = pg.oper_check (
            uut,
            ('show_interface_<WORD>', [], {'ifname':if_name}),
            attrValPairsToCheck,
            refresh_cache=True)
        result = pgcheck.parse()
        log.info("Parsing result : {}".format(result))
        if result:
            log.info("Parsing details : {}".format(pg.ext_dictio[uut.name]))
        else:
            log.error(str(pgcheck))


    @aetest.test
    def pythonTabularParsing(   self,
                                uut,
                                show_arp_header_fields,
                                show_arp_table_title_pattern,
                                show_arp_table_parse_index):
        """ Native Python Parsing of tabular CLI output"""

        res = pg.oper_fill_tabular(device=uut,
                                    show_command="SHOW_ARP",
                                    refresh_cache=True,
                                    header_fields=show_arp_header_fields,
                                    index = show_arp_table_parse_index,
                                    table_title_pattern = \
                                        show_arp_table_title_pattern)
        log.info("Tabular parse result:\n" + pprint.pformat(res.entries))



    @aetest.cleanup
    def do_some_cleaning(self):
        """ testcase clean up """
        log.info("Testcase cleanup")

########################################################################
####                       COMMON CLEANUP SECTION                    ###
########################################################################
#
## Remove the BASE CONFIGURATION that was applied earlier in the
## common cleanup section, clean the left over

class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test """


if __name__ == '__main__': # pragma: no cover
    aetest.main()
