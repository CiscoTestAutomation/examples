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
# the common cleanup section. Script also provides an example on how to invoke
# TCL interpreter to call existing TCL functionalities.
###################################################################

try:
    from ats import tcl
    from ats.tcl import KeyedList
except Exception:
    pass

from ats import aetest
from ats.log.utils import banner

import pprint
import re
import logging
from genie import parsergen as pg
from genie.parsergen.examples.parsergen.pyAts import parsergen_demo_mkpg
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

parameters = {}

#http://code.activestate.com/recipes/576644-diff-two-dictionaries/
class DictDiffer(object):
  """
  Calculate the difference between two dictionaries as:
  (1) items added
  (2) items removed
  (3) keys same in both but changed values
  (4) keys same in both and unchanged values
  """
  def __init__(self, current_dict, past_dict):
    self.current_dict, self.past_dict = current_dict, past_dict
    self.set_current, self.set_past = set(current_dict.keys()), set(past_dict.keys())
    self.intersect = self.set_current.intersection(self.set_past)
  def added(self):
    return self.set_current - self.intersect
  def removed(self):
    return self.set_past - self.intersect
  def changed(self):
    return set(o for o in self.intersect if self.past_dict[o] != self.current_dict[o])
  def unchanged(self):
    return set(o for o in self.intersect if self.past_dict[o] == self.current_dict[o])



###################################################################
###                  COMMON SETUP SECTION                       ###
###################################################################

# Configure and setup all devices and test equipment in this section.
# This should represent the BASE CONFIGURATION that is applicable
# for the bunch of test cases that would follow.

class common_setup(aetest.CommonSetup):
    """ Common Setup for Sample Test """
    @aetest.subsection
    def connect(self, testbed, uut_name, stdby_name):
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
        uut.connect(alias='myuut')


        # Make sure that the connection went fine
        if not hasattr(uut.myuut, 'execute'):
            self.failed()

        if uut.myuut.execute !=  uut.connectionmgr.myuut.execute:
            self.failed()

        log.info ("STEP %s: Device Connection Passed" %
                  (self.parameters['testStep']))

    @aetest.subsection
    def show_exec(self, uut):
        """ common setup subsection: exec show command """
        self.parameters['testStep'] += 1
        log.info(banner("STEP %s: Device Execution Show CMD" %
                      (self.parameters['testStep'])))

        log.info ("show clock")
        # Sending show clock to the device as an execute cmd
        output = uut.myuut.execute('show clock')
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
    """This test case parses the same output with TCL/cAAs and parsergen"""
    @aetest.setup
    def tc_one_setup(self):
        """ test setup """
        log.info("Pass testcase setup")


    @aetest.test
    def tclPythonNonTabularParsingComparison(self, uut, if_name, mtu):
        """ Comparison between TCL and Native Python Parsing """


        if hasattr(uut.myuut, 'handle'):
            tcl.eval('package require cAAs')
            kwargs = {'device' : uut.myuut.handle,
                      'exec' : 'show interface {}'.format(if_name)}
            result = tcl.q.abstract(**kwargs)
            if result[0]:
                parseresult_tcl = dict(KeyedList.from_tcl(result[1]))

                # Massage the key names so that they can be compared with the
                # native Python parser

                new_parseresult_tcl = {}
                for key in parseresult_tcl:
                    new_parseresult_tcl['show.intf.'+key] = parseresult_tcl[key]
                parseresult_tcl = new_parseresult_tcl

                log.info(parseresult_tcl)

        attrValPairsToParse = [
            ('show.intf.if_name',          if_name),
        ]
        pgfill = pg.oper_fill (
            device=uut,
            device_conn_alias='myuut',
            show_command=('show_interface_<WORD>', [], {'ifname':if_name}),
            attrvalpairs=attrValPairsToParse,
            refresh_cache=True, regex_tag_fill_pattern='show\.intf')
        result = pgfill.parse()
        log.info("Parsing result : {}".format(result))

        if hasattr(uut.myuut, 'handle'):
            if result:
                parseresult_python = pg.ext_dictio[uut.myuut.name]
                log.info("Parsing details : {}".format(parseresult_python))
                diff = DictDiffer(parseresult_python, parseresult_tcl)
                log.info("\nTCL vs Python parse comparison analysis:")
                log.info("\nKeys present in TCL but not present in Python : {}".
                    format(diff.removed()))
                log.info("\nKeys present in Python but not present in TCL : {}".
                    format(diff.added()))
                if diff.changed():
                    log.info("\nThe following values differed between TCL and Python :")
                    for key in diff.changed():
                        log.info("Key : {}, TCL value : {}, Python value : {}".
                            format(key, parseresult_tcl[key],
                                   parseresult_python[key]))
            else:
                log.error(str(pgfill))


        attrValPairsToCheck = [
            ('show.intf.if_name',          if_name),
            ('show.intf.line_protocol',    'up'),
            ('show.intf.mtu',              mtu),
            ('show.intf.admin_state',      'up'),
        ]

        pgcheck = pg.oper_check (
            device=uut,
            device_conn_alias='myuut',
            show_command=('show_interface_<WORD>', [], {'ifname':if_name}),
            attrvalpairs=attrValPairsToCheck,
            refresh_cache=True)
        result = pgcheck.parse()
        log.info("Parsing result : {}".format(result))
        if result:
            log.info("Parsing details : {}".format(pg.ext_dictio[uut.myuut.name]))
        else:
            log.error(str(pgcheck))

        #
        # Show all interfaces, ensure the correct section of the output gets
        # parsed.
        #
        pgcheck = pg.oper_check (
            device=uut,
            device_conn_alias='myuut',
            show_command=('show_interface_<WORD>', [], {'ifname':''}),
            attrvalpairs=attrValPairsToCheck,
            refresh_cache=True)
        result = pgcheck.parse()
        log.info("Parsing result : {}".format(result))
        if result:
            log.info("Parsing details : {}".format(pg.ext_dictio[uut.myuut.name]))
        else:
            log.error(str(pgcheck))


    @aetest.test
    def pythonTabularParsing(
                                self,
                                uut,
                                show_arp_header_fields,
                                show_arp_table_title_pattern,
                                show_arp_table_parse_index):
        """ Native Python Parsing of tabular CLI output"""

        res = pg.oper_fill_tabular(device=uut,
                                   device_conn_alias='myuut',
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
