import os

from pyats import aetest

# Needed for logic
from pyats.datastructures.logic import And, Not, Or
from genie.harness.main import gRun

def main():
    test_path = os.path.dirname(os.path.abspath(__file__))
    gRun(
        trigger_datafile=test_path+'/blitz.yaml',
        subsection_datafile=test_path+'/subsection_datafile.yaml',
        mapping_datafile=test_path+'/mapping_datafile.yaml',
        trigger_groups=And('all'),
    )
