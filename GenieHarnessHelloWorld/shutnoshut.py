import time
import logging
from ats import aetest

### Code replaced by using Verification!
#from genie.utils.diff import Diff
###
from genie.harness.base import Trigger

log = logging.getLogger()

class ShutNoShutBgp(Trigger):
    '''Shut and unshut bgp'''

    @aetest.setup
    def prerequisites(self, uut):
        '''Figure out if bgp is configured and up'''

        # To verify if bgp is configured
        output = uut.parse('show bgp process vrf all')

        # Check if there is a bgp_id
        # And it is running
        if not 'bgp_tag' in output:
            # No Bgp! So can't do
            self.skipped("No Bgp is configured for "\
                         "device '{d}'".format(d=uut.name))

        # Now see if its up
        if 'bgp_protocol_state' not in output or\
           output['bgp_protocol_state'] != 'running':
            self.skipped("Bgp is not operational on "
                         "device '{d}'".format(d=uut.name))

        # Keep track of it
        self.bgp_id = output['bgp_tag']
        ### Code replaced by using Verification!
        #self.initial_output = output
        ###

    @aetest.test
    def shut(self, uut):
        '''Shut bgp'''
        uut.configure('''\
router bgp {id}
shutdown'''.format(id=self.bgp_id))

    @aetest.test
    def verify(self, uut):
        '''Verify if the shut worked'''
        # Check if there is a bgp_id
        # And it is running
        output = uut.parse('show bgp process vrf all')
        if output['bgp_tag'] != self.bgp_id:
            self.failed("Bgp id {bgp_id} is not showing anymore in the "
                        "output of the cmd, this is "
                        "unexpected!".format(bgp_id=self.bgp_id))

        # Now see if its down
        if output['bgp_protocol_state'] != 'shutdown':
            self.failed("Shut on Bgp {bgp_id} did not work as it is not "
                        "shutdown".format(bgp_id=self.bgp_id))

    @aetest.test
    def unshut(self, uut):
        '''Shut bgp'''
        uut.configure('''\
router bgp {id}
no shutdown'''.format(id=self.bgp_id))

    @aetest.test
    def verify_recover(self, uut, wait_time=20):
        '''Figure out if bgp is configured and up'''
        ### Code replaced by using Verification!
        #log.info('Sleeping for {w}'.format(w=wait_time))
        #time.sleep(wait_time)
        ###

        # Check if there is a bgp_id
        # And it is running
        output = uut.parse('show bgp process vrf all')
        if output['bgp_tag'] != self.bgp_id:
            self.failed("Bgp id {bgp_id} is not showing anymore in the "
                        "output of the cmd, this is "
                        "unexpected!".format(bgp_id=self.bgp_id))

        # Now see if its down
        if output['bgp_protocol_state'] != 'running':
            self.failed("Reconfigure of Bgp {bgp_id} did not work as it is not "
                        "running".format(bgp_id=self.bgp_id))

        ### Code replaced by using Verification!
        #diff = Diff(self.initial_output, output)
        #diff.findDiff()
        #if diff.diffs:
        #    self.failed('Unexpected change has happened to our device state '
        #                '\n{d}'.format(d=diff))
        ### 
