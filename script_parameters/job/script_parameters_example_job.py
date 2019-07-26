# To run the job:
# pyats run job $VIRTUAL_ENV/examples/script_args/job/script_args_example_job.py
# Description: This example shows how to pass script args from the job file
#              (and then how to read/set them from the script)

import os
from pyats.easypy import run

def main():
    # Find the location of the script in relation to the job file
    test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    testscript = os.path.join(test_path, 'script_parameters_example_script.py')
    
    run(testscript=testscript, x=1, y=2)
