#!/bin/env python
###################################################################
# basic_example.py : A very simple test script example which include:
#     common_setup
#     Tescases
#     common_cleanup
# The purpose of this sample test script is to show the "hello world"
# of aetest.
###################################################################

# To get a logger for the script
import logging

# Needed for aetest script
from ats import aetest

# Genie Imports
from genie.harness.standalone import run_genie_sdk, GenieStandalone
from genie.conf import Genie

# Verifications classes and template class which is used for verifications
# using parser or Genie Ops.

# Get your logger for your script
log = logging.getLogger(__name__)

###################################################################
###                  COMMON SETUP SECTION                       ###
###################################################################

# This is how to create a CommonSetup
# You can have one of no CommonSetup
# CommonSetup can be named whatever you want

class common_setup(aetest.CommonSetup):
    """ Common Setup section """

    # CommonSetup have subsection.
    # You can have 1 to as many subsection as wanted
    # here is an example of 2 subsections

    # First subsection
    @aetest.subsection
    def sample_subsection_1(self):
        """ Common Setup subsection """
        log.info("Aetest Common Setup ")

    @aetest.subsection
    def connect(self, testbed):
        pass
        #genie_testbed = Genie.init(testbed)
        #self.parent.parameters['testbed'] = genie_testbed
        #uut = genie_testbed.devices['uut']
        #uut.connect()

    # If you want to get the name of current section,
    # add section to the argument of the function.

    # Second subsection
    @aetest.subsection
    def sample_subsection_2(self, section):
        """ Common Setup subsection """
        log.info("Inside %s" % (section))

        # And how to access the class itself ?

        # self refers to the instance of that class, and remains consistent
        # throughout the execution of that container.
        log.info("Inside class %s" % (self.uid))

###################################################################
###                     TESTCASES SECTION                       ###
###################################################################

# This is how to create a testcase
# You can have 0 to as many testcases as wanted
class tc_one(aetest.Testcase):
    # First test section
    @ aetest.test
    def simple_test_1(self):
        """ Sample test section. Only print """
        log.info("First test section ")

    # Second test section
    @ aetest.test
    def simple_test_2(self):
        """ Sample test section. Only print """
        log.info("Second test section ")

# You can also create testcase based on Genie Triggers
# Testcase name : tc_one
class tc_genie_trigger(GenieStandalone):
    """ This is testcase created dynamically from existing
    Trigger/Verification """
    # This will create multiple sections 
    # TriggerShutNoShutBgp
    # TriggerSleep
    triggers = ['TriggerShutNoShutBgp', 'TriggerSleep']
    order = ['TriggerShutNoShutBgp', 'TriggerSleep']

# You can also call Triggers and Verifications within a pyATS section
class tc_pyats_genie(aetest.Testcase):
    # First test section
    @ aetest.test
    def simple_test_1(self, steps):
        """ Sample test section. Only print """
        log.info("First test section ")

        # Run genie triggers and verifications
        run_genie_sdk(self, steps,
                      ['Verify_BgpVrfAllAll', 'TriggerSleep', 'TriggerShutNoShutBgp',
                       'TriggerSleep', 'Verify_BgpVrfAllAll'])

    # Second test section
    @ aetest.test
    def simple_test_2(self):
        """ Sample test section. Only print """
        log.info("Second test section ")

# Testcase name : tc_one
# You can also combine both together!
class tc_pyats_and_genie_trigger(GenieStandalone):
    """ This is user Testcases section """
    triggers = ['TriggerShutNoShutBgp', 'TriggerSleep']
    order = ['TriggerShutNoShutBgp', 'prepare_testcase', 'TriggerSleep']

    # This is how to create a setup section
    @aetest.setup
    def prepare_testcase(self, steps, section):
        """ Testcase Setup section """
        with steps.start('bla'):
            print('ww')

        log.info("Preparing the test")
        log.info(section)
        run_genie_sdk(self, steps,
                      ['TriggerSleep', 'TriggerShutNoShutBgp', 'TriggerSleep'])
        run_genie_sdk(self, steps,
                      ['Verify_BgpVrfAllAll', 'TriggerShutNoShutBgp',
                       'TriggerSleep', 'TriggerShutNoShutBgpNeighbors'])

#####################################################################
####                 Genie Harness information                    ###
#####################################################################

# Run verification
# Enter the name of the verification name which
# matches the one in the datafile.
#
class Verify_bgp(GenieStandalone):
    verifications = ['Verify_BgpVrfAllAll']

class TriggerSleep(GenieStandalone):
    triggers = ['TriggerSleep']

class TriggerSleep(GenieStandalone):
    '''Custom arguments can be provided to overwrite the datafile information'''
    triggers = ['TriggerSleep']
    custom_arguments = {'TriggerSleep': {'message_time':2}}

class Trigger_verification_mix(GenieStandalone):
    verifications = ['Verify_BgpVrfAllAll']
    triggers = ['TriggerShutNoShutBgp', 'TriggerSleep']

    order = ['Verify_BgpVrfAllAll', 'TriggerShutNoShutBgp', 'TriggerSleep', 'Verify_BgpVrfAllAll', 'bla']

    timeout = {'interval':2, 'max_time':300}

    custom_arguments = {'TriggerShutNoShutBgp': {'tgn_max_outage': 2, 'timeout':{'interval':5, 'max_time':300}}}

    @aetest.test
    def bla(self):
        log.info('qweqe')

#####################################################################
####                       COMMON CLEANUP SECTION                 ###
#####################################################################

# This is how to create a CommonCleanup
# You can have 0 , or 1 CommonCleanup.
# CommonCleanup can be named whatever you want :)
class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test """

    # CommonCleanup follow exactly the same rule as CommonSetup regarding
    # subsection
    # You can have 1 to as many subsections as wanted
    # here is an example of 1 subsection

    @aetest.subsection
    def clean_everything(self):
        """ Common Cleanup Subsection """
        log.info("Aetest Common Cleanup ")

if __name__ == '__main__': # pragma: no cover
    aetest.main()
