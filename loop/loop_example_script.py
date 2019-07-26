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
    @aetest.subsection.loop(uids=[1,2])
    def common_setup_subsection_one(self):
        """ Common Setup subsection """
        log.info(banner(" Aetest Common Setup "))

    @aetest.subsection.loop(looping_var=[1,2])
    def common_setup_subsection_two(self, looping_var):
        """ Common Setup subsection """
        log.info(banner(" Aetest Common Setup "))
        log.info('called with looping var %s' % looping_var)

###################################################################
###                     TESTCASES SECTION                       ###
###################################################################

class my_looped_testcase(aetest.Testcase):
    @aetest.setup
    def empty_setup(self):
        """ Testcase Setup section """
        log.info ("---------------empty_setup-------------------")

    @aetest.test.loop(uids=['1-123',2])
    def test_one(self):
        log.info ("---------------TEST1 LOOP-------------------")
        log.info ("Test Iteration in testcase test1 section")

    def vfunc():
        return ['a','b']
    
    @aetest.loop(uids=vfunc)
    @aetest.test
    def test_two(self):
        log.info ("---------------TEST2 LOOP-------------------")
        log.info ("Test Iteration in testcase test2 section")


#####################################################################
####                       COMMON CLEANUP SECTION                 ###
#####################################################################

class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test """
    @aetest.subsection
    def common_cleanup_subsection(self):
        """ Common Cleanup Subsection """
        log.info(banner(" Aetest Common Cleanup "))

if __name__ == "__main__": # pragma: no cover
    aetest.main()
