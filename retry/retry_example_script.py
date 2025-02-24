#!/usr/bin/env python
###################################################################
# retry_example_script.py
# The purpose of the sample test script is to test the retry
# functionality on testcases and testsections
###################################################################

import logging
from pyats import aetest

logger = logging.getLogger(__name__)

# retry feature can be enabled by @aetest.retry()
# It takes in args 
# retries - Number of retries
# retry_wait - wait time between retries

@aetest.retry(retries=2, retry_wait=2)
class MyTestcase_1(aetest.Testcase):

    # define setup section
    @aetest.setup
    def testcase_setup(self):
        pass
        
    # In this section there is an intentional failure. When
    # the retry_count is 2 we mark the testsection as [passed].
    # Here retry and retry_count are optional parameters, that
    # can be used in the script
    #   retry(bool) - To check if the section is retried
    #   retry_count(int) - To keep in track of retry count

    @aetest.retry(retries=2, retry_wait=2)
    @aetest.test
    def connect_testcase(self, steps, retry, retry_count):
        if retry_count==2:
            self.passed()
        self.failed('This is an intentional failure from connect_testcase')

    @aetest.retry(retries=2, retry_wait=2)
    @aetest.test
    def testcase_test(self):
        pass        

       
if __name__ == '__main__':
    aetest.main()

