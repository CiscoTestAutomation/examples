# To run the job:
# pyats run job task_example_job.py
# Description: This example demonstrate how tasks in easypy jobfiles are
#              created and handled.

import os
from pyats.easypy import Task

def main():
    # Find the location of the script in relation to the job file
    test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    testscript = os.path.join(test_path, 'task_example.py')

    # create two tasks. for simplicity's sake, we'll reuse the same script
    task_1 = Task(testscript = testscript)
    task_2 = Task(testscript = testscript)

    # start both tasks together (async execution)
    task_1.start()
    task_2.start()

    # wait for tasks to finish before terminating
    task_1.wait()
    task_2.wait()
