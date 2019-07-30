'''demo11_harness_cluster_job.py

Please read the README file.
'''

#
# optional author information
#
__author__ = 'Cisco Systems Inc.'
__copyright__ = 'Copyright (c) 2018, Cisco Systems Inc.'
__contact__ = ['pyats-support-ext@cisco.com']
__date__= 'April 2019'

#
# import block
#
import os

from genie.harness.main import gRun

def main():
    test_path = os.path.dirname(os.path.abspath(__file__))

    # mapping_datafile is mandatory
    # trigger_uids limit which test to execute
    gRun(trigger_uids=['TriggerCluster'],
         verification_uids=['Verify_BgpVrfAllAll.uut', 'Verify_Interface.uut'],
         trigger_datafile='trigger_datafile.yaml')
