#!/usr/bin/env python
###################################################################
# uids_example_script.py : Demonstrate how to Execute/skip particular test
# By default is there is uids is not defined, everything is
# executed.
# If uids is defined, only what match true with uids will be executed
###################################################################

# To get a logger for the script
import logging

# Needed for aetest script
from pyats import aetest

# Get your logger for your script
log = logging.getLogger(__name__)

###################################################################
###                  COMMON SETUP SECTION                       ###
###################################################################

# CommonSetup will also be skipped if it is not mentioned in the uids
class common_setup(aetest.CommonSetup):
    """ Common Setup section """
    @aetest.subsection
    def common_setup_subsection(self):
        """ Common Setup subsection """
        log.info("Aetest Common Setup")

###################################################################
###                     TESTCASES SECTION                       ###
###################################################################

class my_looped_testcase(aetest.Testcase):
    @aetest.setup
    def empty_setup(self):
        """ Testcase Setup section """
        pass

    # Each loop can be singly skipped, we have an example of loop2 being
    # skipped but not loop1
    @aetest.loop(['loop1', 'loop2'])
    @aetest.test
    def test_one(self, section):
        log.info ("---------------TEST1 LOOP-------------------")
        log.info ("Test Iteration in testcase %s section" % (section,))

    # We have an example which skips ^loop2. This will not be skipped, as it
    # does not match the regex expression.
    @aetest.test
    def test_two_loop2(self):
        log.info ("Test Iteration in testcase test_two_loop2 section")

class tc_two(aetest.Testcase):
    """ This is user Testcases section """
    @aetest.setup
    def tc_two_setup(self):
        pass

    @aetest.cleanup
    def tc_two_cleanup(self):
        """ Testcase cleanup section """
        pass
#####################################################################
####                       COMMON CLEANUP SECTION                 ###
#####################################################################

# CommonCleanup will be skipped if not mentioned in the uids list to be executed
class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test """
    @aetest.subsection
    def common_cleanup_subsection(self):
        """ Common Cleanup Subsection """
        log.info("Aetest Common Cleanup")

if __name__ == "__main__": # pragma: no cover
    aetest.main()
