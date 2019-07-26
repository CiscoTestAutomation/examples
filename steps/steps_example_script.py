#!/usr/bin/env python
###################################################################
# step_example.py : A simple example with test
#     common_setup section
#     Tescases section
#     common_cleanup section
# The purpose of the sample is to demonstrate how to use step
###################################################################

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
    def check_env(self, steps, testbed = None):
        """ Common Setup subsection """
        log.info(banner(" Aetest Common Setup "))

        if testbed:
            for device in testbed.devices:
                testbed.devices[device].connect()

        # Example of a single test all alone
        # Roll up to passed
        with steps.start('myStep1',continue_=True) as step:
            pass

        with steps.start('myStep2',continue_=True) as step:
            step.passed()

###################################################################
###                     TESTCASES SECTION                       ###
###################################################################

class tc_one(aetest.Testcase):
    """ This is user Testcases section """

    @aetest.test
    def test_one(self, steps):
        """ Testcase Setup section """
        log.info(banner(" Aetest Testcase Execution "))

        # Example of multiple steps
        with steps.start('chiq') as step:
            step.passed()
        with steps.start('chiq') as step:
            step.passx()
        with steps.start('chiq',continue_=True) as step:
            step.failed()
        with steps.start('chiq',continue_=True) as step:
            step.skipped()

    @aetest.test
    def testChild(self, steps):

        # Child test
        # Example of child step. Usuaully you would pass step to a func
        # But it is up to the user to decide what to do with it. 
        # Please check testChildFunc below for an example
        # where a func is called
        with steps.start('chiq',continue_=True) as step:
            with step.start('child1') as child:
                child.passed()
            with step.start('child2') as child:
                child.passed()
            with step.start('child3') as child:
                child.passed()
            with step.start('child4',continue_=True) as child:
                child.skipped()
            step.passed()

    @aetest.test
    def testChildFail(self, steps):

        # Child test
        # Example of child step. Usually you would pass step to a func
        # But it is up to the user to decide what to do with it. 
        with steps.start('chiq',continue_=True) as step:
            with step.start('child1') as child:
                child.failed()
            with step.start('child2') as child:
                child.failed()
            with step.start('child3') as child:
                child.failed()
            with step.start('child4') as child:
                child.skipped()
            step.passed()

    @aetest.test
    def testChildFunc(self, steps):
        # Child test
        with steps.start('chiq',continue_=True) as step:
            try:
                # Example of when passing a child
                myFunc(step=step)
                # Example when not passing a child
                myFunc()
            except Exception:
                step.failed()
            else:
                step.passed()

# Container for defaulting step to 
from pyats.aetest.steps import Steps
def myFunc(step=Steps()):
    ''' No Code modification when passing a child or not '''
    with step.start('child1') as child:
        child.passed()
    with step.start('child2') as child:
        child.passed()
    with step.start('child3') as child:
        child.passed()
    with step.start('child4') as child:
        child.passed()


#####################################################################
####                       COMMON CLEANUP SECTION                 ###
#####################################################################

class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test """
    @aetest.subsection
    def clean_everything(self):
        """ Common Cleanup Subsection """
        log.info(banner(" Aetest Common Cleanup "))

if __name__ == '__main__': # pragma: no cover
    aetest.main()
