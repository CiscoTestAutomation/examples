# To run the job:
# pyats run job features_example_job.py
# Description: This example shows an overview of the different features/flows
#              that pyATS supports like skipping testcases, looping, variants,
#              in addition to basic usage (passing/failing/etc)

import os
from pyats.easypy import run
from pyats.datastructures.logic import Not

def main():
    # Find the location of the script in relation to the job file
    test_path = os.path.dirname(os.path.abspath(__file__))
    testscript = os.path.join(test_path, 'features_example_script.py')

    run(testscript=testscript,
        uids = Not("my_skipped_testcase1", "my_skipped_testcase2"),)
