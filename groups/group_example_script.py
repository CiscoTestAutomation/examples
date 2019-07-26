#!/usr/bin/env python
###################################################################
# execution_group_example.py : Demonstrate how to use groups in aetest
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

class common_setup(aetest.CommonSetup):
    """ Common Setup section """

    @aetest.subsection
    def common_setup_subsection(self):
        """ Common Setup subsection """
        # Groups cannot be set into a subsection
        # Groups then just become a local variable

        # This does nothing, it is a local variable named groups
        groups = ['group2']

###################################################################
###                     TESTCASES SECTION                       ###
###################################################################

class my_looped_testcase(aetest.Testcase):
    # Associate this testcase and all its loop variation to group1
    # you can associate a testcase with as many group as wanted
    # As section cannot have a group, they do what the testcase do
    groups = ['group1']

    @aetest.test
    def test_one(self):
        log.info ("Test Iteration in testcase test1 section")

    # Loop also follows its testcase group
    @aetest.loop(['loop1', 'loop2'])
    @aetest.test
    def test_two(self):
        log.info ("---------------LOOP-------------------")

class tc_two(aetest.Testcase):
    """ This is user Testcases section """
    # Associate this testcase two groups: group2 and group3
    groups = ['group2', 'group3']

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
class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test """

    @aetest.subsection
    def common_cleanup_subsection(self):
        """ Common Cleanup Subsection """
        log.info(" Aetest Common Cleanup ")

# Used for Standalone mode
if __name__ == "__main__": # pragma: no cover
    aetest.main()
