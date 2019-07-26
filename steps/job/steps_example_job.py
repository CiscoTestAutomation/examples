# To run the job:
# pyats run job $VIRTUAL_ENV/examples/steps/job/steps_example_job.py
# Description: This example shows the basic functionality of pyats 
#              with few passing tests

import os
from pyats.easypy import run

def main():
    # Find the location of the script in relation to the job file
    test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    testscript = os.path.join(test_path, 'steps_example_script.py')
    stepDebug = os.path.join(test_path, 'etc','stepsDebug.yaml')

    run(testscript=testscript,
        step_debug=stepDebug)
