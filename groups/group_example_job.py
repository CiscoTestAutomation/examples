# To run the job:
# pyats run job group_example_job.py
# Description: This example shows looping and variants in pyats

import os

from pyats.easypy import run
# Data structure used to mentions that to execute
from pyats.datastructures.logic import And, Or, Not

def main():
    # Find the location of the script in relation to the job file
    test_path = os.path.dirname(os.path.abspath(__file__))
    testscript = os.path.join(test_path, 'group_example_script.py')

    #Task-1
    # Execution Group by itself
    # Only execute group1
    run(testscript=testscript,
        groups=Or('group1'))

    #Task-2
    # Execute testcases that are member of group1 and group2
    # We expect only the common_ to be executed, no testcase
    run(testscript=testscript,
        groups=And('group1', 'group2'))

    #Task-3
    # Execute testcases that are member of group1 and group3
    # We expect tc_two to be executed
    run(testscript=testscript,
        groups=And('group2', 'group3'))

    #Task-4
    # Combine groups and ids.
    # Execute testcase part of Group 1 or Group2 , and not tc_two
    # We expect everything except tc_two to be executed
    run(testscript=testscript,
        groups=Or('group1', 'group2'),
        uids=Not('tc_two'))

    # Create a function that tests for testcases group
    # this api tests that a testcase belongs to group 1 but not group 2
    # The argument must be stared
    def group1_not_group2(*groups):
        # Groups is evaluated on run time,  will be replaced by the groups of
        # the testcase
        # Return True/False
        # if True the testcase will execute
        return 'group1' in groups and 'group2' not in groups

    #Task-5
    # Use the above function as group callable
    # we expect everything except tc_two to be executed
    run(testscript=testscript,
        groups=group1_not_group2)
