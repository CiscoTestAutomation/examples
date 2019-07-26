#!/usr/bin/env python
import logging
from pyats import aetest
from pyats.log.utils import banner

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

###################################################################
###                  COMMON SETUP SECTION                       ###
###################################################################

# As a simple example, we don't do much here except printing some 
# log messages.

class common_setup(aetest.CommonSetup):
    """ Common Setup section """
    @aetest.subsection
    def common_setup_subsection(self, x, y):
        """ Common Setup subsection """
        log.info(banner(" Aetest Common Setup "))
        # Use script args from aetest
        print("Script args from common setup")
        print(x)
        assert x == 1

###################################################################
###                     TESTCASES SECTION                       ###
###################################################################

class tc_one(aetest.Testcase):
    """ This is user Testcases section """
    @aetest.setup
    def tc_one_setup(self, x):
        """ Testcase Setup section """
        log.info(banner(" Aetest Testcase Execution "))
        print("Script args from testcase")
        assert x == 1

    @aetest.test
    def tc_one_test(self):
        pass

    @aetest.cleanup
    def tc_one_cleanup(self):
        """ Testcase cleanup section """
        log.info("Pass testcase cleanup")
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
