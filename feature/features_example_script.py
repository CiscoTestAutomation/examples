#!/usr/bin/env python
###################################################################
# test_sample1.py : A very simple test script example which include:
#     common_seup section
#     Tescases section
#     common_cleanup section
# The purpose of the sample test script is to show the "hello world"
# of the pyaetest.
###################################################################

import logging
from pyats import aetest
from pyats.log.utils import banner

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

###################################################################
###                  COMMON SETUP SECTION                       ###
###################################################################

# As a simplest example, we don't do much here except printing some 
# log messages.

class common_setup(aetest.CommonSetup):
    """ Common Setup section """
    @aetest.subsection
    def common_setup_subsection(self):
        """ Common Setup subsection """
        log.info(banner(" Aetest Common Setup "))

###################################################################
###                     TESTCASES SECTION                       ###
###################################################################

class my_passing_tc(aetest.Testcase):
    """ This is user Testcases section """
    @aetest.setup
    def tc_setup(self):
        """ Testcase Setup section """
        log.info(banner(" Aetest Testcase Execution "))


    @aetest.test
    def tc_test(self):
        """ test section """
        log.info("test")


    @aetest.cleanup
    def tc_cleanup(self):
        """ Testcase cleanup section """
        log.info("Pass testcase cleanup")
    
class my_failed_testcase(aetest.Testcase):
    """ This is user Testcases - fail on purpose"""
    @aetest.setup
    def tc_setup(self):
        """ Testcase Setup section """
        log.error("Trying to fail the test case!")
        self.failed()

class my_skipped_testcase1(aetest.Testcase):
    """ This is user Testcases - skip on purpose"""
    @aetest.setup
    def tc_setup(self):
        """ Testcase Setup section """
        log.warning("Trying to skip the test case!")

    @aetest.test
    def tc_test(self):
        """ test section """
        log.info("dumb test")

    @aetest.cleanup
    def tc_clean(self):
        pass

class my_skipped_testcase2(aetest.Testcase):
    """ This is user Testcases - skip on purpose"""
    @aetest.setup
    def tc_setup(self):
        """ Testcase Setup section """
        log.warning("Trying to skip the test case!")

    @aetest.test
    def tc_test(self):
        """test section """
        log.info("dumb test")

    @aetest.cleanup
    def tc_clean(self):
        pass

@aetest.loop(['loop1', 'loop2'])
class my_looped_testcase(aetest.Testcase):
    @aetest.test
    def printValue(self):
        log.info ("---------------TEST LOOP-------------------")
        log.info("Test UID: %s" %(self.uid))

@aetest.loop(variants=[1,2])
class my_looped_testcase_variant(aetest.Testcase):
    @aetest.test
    def printValue(self, variants):
        log.info ("---------------TEST LOOP2-------------------")
        log.info ("Test Iteration variant: %s" % variants)
        log.info("Test UID: %s" %(self.uid))
#####################################################################
####                       COMMON CLEANUP SECTION                 ###
#####################################################################

class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test """
    @aetest.subsection
    def common_cleanup_subsection(self):
        """ Common Cleanup Subsection """
        log.info(banner(" Aetest Common Cleanup "))

if __name__ == '__main__': # pragma: no cover
    aetest.main()
