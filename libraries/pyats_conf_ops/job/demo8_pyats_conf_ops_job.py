import os
import argparse
from ats.easypy import run

parser = argparse.ArgumentParser()

parser.add_argument('--context',
                help='Type agnostic to execute the script with',
                choices=['cli', 'yang', 'xml'],
                default = 'cli')
parser.add_argument('--pool_num',
                help='Number of connections to used in the pool',
                type=int, default=1)
parser.add_argument('--uut_alias',
                help='Alias name for the uut device',
                type=str, default='uut')
parser.add_argument('--helper_alias',
                help='Alias name for the helper device',
                type=str, default='helper')

# All run() must be inside a main function
def main():
    # Find the location of the script in relation to the job file
    custom_args = parser.parse_known_args()[0]
    test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    testscript = os.path.join(test_path, 'demo8_pyats_conf_ops.py')
    datafile = os.path.join(test_path, 'datafile.yaml')

    # Execute the testscript
    run(testscript=testscript,
        uut_alias=custom_args.uut_alias,
        helper_alias=custom_args.helper_alias,
        context=custom_args.context,
        datafile=datafile,
        pool_num=custom_args.pool_num)
