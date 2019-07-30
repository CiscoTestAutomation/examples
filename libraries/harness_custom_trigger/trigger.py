# Python
import time
import logging

# pyATS
from ats import aetest

# Genie
from genie.harness.base import Trigger

# Parser
from genie.libs.parser.nxos.show_arp import ShowIpArp

# Metaparser exception
from genie.metaparser.util.exceptions import SchemaEmptyParserError

log = logging.getLogger(__name__)

# Steps in this Trigger
# Take snapshot of existing arp
# clear ip arp vrf all force-delete
# Verify they all came back - And uptime was reduced

class TriggerClearArpVrfAllForceDelete(Trigger):

    @aetest.setup
    def verify_prerequisite(self, uut):
        ''' '''

        # Perform init steps here
        # Call our parser
        parser = ShowIpArp(device=uut)
        output = parser.parse()
        self.initial_output = {}

        for addr, value in output.items():
            if 'age' in value:
                self.initial_output[addr] = {}
                self.initial_output[addr]['age'] = value['age']

    @aetest.test
    def clear(self, uut):

        log.info('Send Clear cmd')
        uut.execute('clear ip arp vrf all force-delete')

    @aetest.test
    def verify_clear(self, uut, sleep):

        time.sleep(sleep)
        # Call our parser
        parser = ShowIpArp(device=uut)
        try:
            after_output = parser.parse()
        except SchemaEmptyParserError:
            # If only 1 arp, then it will return empty, which is perfectly fine
            pass

        for addr, value in self.initial_output.items():
             if addr not in after_output:
                 # Lost an arp!
                 self.failed('Lost {addr}'.format(addr=addr))


             # Make sure uptime is less than 30 sec
             if not after_output[addr]['Age'] == '-' and\
                after_output[addr]['Age'] > 30 or\
                after_output[addr]['Age'] > self.initial_output[addr]['Age']:
                 self.failed('{addr} was not reseted'.format(addr=addr))
