'''comprehensive_testcases.py

This file contains some common testcases used by comprehensive base and variant
examples. It serves as an example demonstrating the usage & benefits of using
testcase files.

For more on testcase files, refer to __init__.py of testcases/ folder.

Note:
   Any comments with "#*" in front of them (like this entire comment box) are
   for example/infrastructure clarifications only.

Author:
   Siming Yuan, Cisco Systems Inc.

Support:
   pyats-support-ext@cisco.com

'''


#
# import statements
#
from pyats import aetest
import logging

#
# create a logger for this module
#
logger = logging.getLogger(__name__)

#*******************************************************************************
#* TESTCASE DEFINITIONS
#*
#*  Tach testcase defined here can be imported in main scripts and used. 
#*
#*  The main advantage of defining testcases outside of the scope of testscripts
#*  is the ability to abstract out the test data required by the testcase. This
#*  allows testcases to be re-useable (instead of being hard-coded with values).
#*  
#*  This data-test abstraction is a supplement to testcase parameters.
#*
#*******************************************************************************


#******************************
#* Dynamic Loop Testcase
#*
#*  this testcase demonstrate dynamic looping: defining loops dynamically within
#*  test sections (as opposed to static looping using the @loop decorator).
class DynamicLoopDemonstration(aetest.Testcase):
    '''Dynamic Loop Demonstration

    This testcase requires some data in order to run. These data needs to be
    defined when the testcase is inherited. 

    Requires Data:
        loop_value_one (list): list of loop values for dynamic looping of
                               test section one
        loop_value_twp (list): list of loop values for dynamic looping of
                               test section two
    '''

    @aetest.setup
    def setup(self):
        '''Setup section

        this section turns on looping of testcase section one and two.
        '''

        #******************************
        #* Dynamic Loop Testcase
        #*  
        #*  Marking sections for looping dynamically is done using function
        #*  'aetest.loop.mark'. To use, pass in the section to be marked for
        #*  looping as the first argument. The rest of the options are exactly
        #*  the same as using @loop decorator.
        #*
        #*  dynamic looping works on both testcases and sections. This example
        #*  is using test sections for demonstration
        #*
        #*  note also that within this definition, we are referring to two
        #*  testcase data attributes: 
        #*      DynamicLoopDemonstration.loop_value_one
        #*      DynamicLoopDemonstration.loop_value_two
        #*
        #*  both needs to be defined when the testcase is inherited.
        aetest.loop.mark(self.test_one, loop_parameter = self.loop_value_one)
        aetest.loop.mark(self.test_two, loop_parameter = self.loop_value_two)


    @aetest.test
    def test_one(self, loop_parameter):
        '''Test one

        Dynamically looped test section one. 
        '''

        logger.info('Loop iteration with parameter value: %s' % loop_parameter)

    @aetest.test
    def test_two(self, loop_parameter):
        '''Test two

        Dynamically looped test section two. 
        '''

        logger.info('Loop iteration with parameter value: %s' % loop_parameter)

    
