# To run the job:
# pyats run job $VIRTUAL_ENV/examples/basic/job/basic_example_job.py
# Description: This example shows the basic functionality of pyats
#              with few passing tests

import os
from ats.easypy import run

# All run() must be inside a main function
def main():
    # Find the location of the script in relation to the job file
    test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    testscript = os.path.join(test_path, 'demo7_trigger_within_pyats.py')

    # Execute the testscript
    run(testscript=testscript)
