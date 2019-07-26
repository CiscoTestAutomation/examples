import os
from pyats.easypy import run

# To run the job:
# pyats run job $VIRTUAL_ENV/examples/connection/job/connection_example_job.py \
#               --testbed-file <your tb file>
#
# Description: This example uses a sample testbed, connects to a device
#              which name is passed from the job file,
#              and executes some commands.

# All run() must be inside a main function
def main():
    # Find the location of the script in relation to the job file
    test_path = os.path.dirname(os.path.abspath(__file__))
    testscript = os.path.join(test_path, 'connection_example_script.py')

    # Execute the testscript
    run(testscript=testscript)
