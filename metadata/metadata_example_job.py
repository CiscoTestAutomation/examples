# To run the job:
# pyats run job basic_example_metadata_job.py
# Description: This example shows the basic functionality of pyats 
#              with few passing tests

import os
from pyats.easypy import run

# All run() must be inside a main function
def main(runtime):
    # Find the location of the script in relation to the job file
    test_path = os.path.dirname(os.path.abspath(__file__))
    testscript = os.path.join(test_path, 'metadata_example.py')
    
    
    runtime.job.release = "1.2.3"
    runtime.job.image = "image1"
    run(testscript=testscript)
    run(testscript=testscript)
