import os

# Needed for logic
from ats.datastructures.logic import And, Not, Or

from genie.harness.main import gRun

def main():

    test_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    gRun(trigger_datafile=os.path.join(test_path, 'trigger_datafile_demo.yaml'))
