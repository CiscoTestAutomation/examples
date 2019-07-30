'''demo4_harness_custom_trigger_job.py

Please read the README file.
'''

#
# optional author information
#
__author__ = 'Cisco Systems Inc.'
__copyright__ = 'Copyright (c) 2018, Cisco Systems Inc.'
__contact__ = ['pyats-support-ext@cisco.com']
__date__= 'April 2018'

#
# import block
#
import os

from genie.harness.main import gRun

def main():
    test_path = os.path.dirname(os.path.abspath(__file__))

    # the trigger_datafile is custom created by the user for a newly developed trigger
    # pts_features mentions to Genie which feature to learn in CommonSetup, and then compare at the CommonCleanup
    # trigger_uids and verification_uids limit which test to execute
    gRun(trigger_datafile=os.path.join(test_path, 'trigger_datafile_demo.yaml'),
         pts_features=['platform', 'bgp', 'interface'],
         verification_uids=['Verify_IpInterfaceBrief', 'Verify_IpRoute_vrf_all'],
         trigger_uids=['TriggerUnconfigConfigBgp.uut', 'TriggerShutNoShutBgpNeighbors', 'TriggerModifyLoopbackInterfaceIp.uut', 'TriggerShutNoShutEthernetInterface', 'TriggerClearArpVrfAllForceDelete'])
