"""
To run the job:
    pyats run job retry_example_job.py
Description: This example shows retry and variants in pyats
"""

import os
from pyats.easypy import run

def main():
    # Find the location of the script in relation to the job file
    test_path = os.path.dirname(os.path.abspath(__file__))
    testscript = os.path.join(test_path, 'retry_example_script.py')
    
    run(testscript=testscript)

