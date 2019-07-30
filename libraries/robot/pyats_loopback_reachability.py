import re
import logging

from ats import aetest
from ats.log.utils import banner

#
# create a logger for this testscript
#
logger = logging.getLogger(__name__)

class PingTestcase(aetest.Testcase):
    '''Ping test'''

    groups = ('basic', 'looping')

    @aetest.test.loop(destination = ('10.0.1.2', '10.0.2.2'))
    def ping(self, device, destination, testbed):
        '''
        ping destination ip address from device
        Sample of ping command result:
        ping
        Protocol [ip]:
        Target IP address: 10.10.10.2
        Repeat count [5]:
        Datagram size [100]:
        Timeout in seconds [2]:
        Extended commands [n]: n
        Sweep range of sizes [n]: n
        Type escape sequence to abort.
        Sending 5, 100-byte ICMP Echos to 10.10.10.2, timeout is 2 seconds:
        !!!!!
        Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
        '''

        try:
            # store command result for later usage
            result = testbed.devices[device].ping(destination)

        except Exception as e:
            # abort/fail the testscript if ping command returns any exception
            # such as connection timeout or command failure
            self.failed('Ping {} from device {} failed with error: {}'.format(
                                destination,
                                device,
                                str(e),
                            ),
                        goto = ['exit'])
        else:
            # extract success rate from ping result with regular expression
            match = re.search(r'Success rate is (?P<rate>\d+) percent', result)
            success_rate = match.group('rate')
            # log the success rate
            logger.info(banner('Ping {} with success rate of {}%'.format(
                                        destination,
                                        success_rate,
                                    )
                               )
                        )


# Ping Testcase: leverage dual-level looping
class NxosPingTestcase(aetest.Testcase):
    '''Ping test'''

    groups = ('basic', 'looping')

    @aetest.test.loop(destination = ('10.0.2.1', '10.0.1.1'))
    def ping(self, device, destination, testbed):
        '''
        ping destination ip address from device
        Sample of ping command result:

        ping
        Vrf context to use [default] :
        Target IP address or Hostname: 192.168.0.6
        Repeat count [5] :
        Packet-size [56] :
        Timeout in seconds [2] :
        Sending interval in seconds [0] :
        Extended commands [no] : n
        Sweep range of sizes [no] : n
        Sending 5, 56-bytes ICMP Echos to 192.168.0.6
        Timeout is 2 seconds, data pattern is 0xABCD

        64 bytes from 192.168.0.6: icmp_seq=0 ttl=254 time=4.774 ms
        64 bytes from 192.168.0.6: icmp_seq=1 ttl=254 time=2.914 ms
        64 bytes from 192.168.0.6: icmp_seq=2 ttl=254 time=3.53 ms
        64 bytes from 192.168.0.6: icmp_seq=3 ttl=254 time=3.015 ms
        64 bytes from 192.168.0.6: icmp_seq=4 ttl=254 time=4.999 ms

        --- 192.168.0.6 ping statistics ---
        5 packets transmitted, 5 packets received, 0.00% packet loss
        round-trip min/avg/max = 2.914/3.846/4.999 ms
        '''

        try:
            # store command result for later usage
            result = testbed.devices[device].ping(destination)

        except Exception as e:
            # abort/fail the testscript if ping command returns any exception
            # such as connection timeout or command failure
            self.failed('Ping {} from device {} failed with error: {}'.format(
                                destination,
                                device,
                                str(e),
                            ),
                        goto = ['exit'])
        else:
            # extract success rate from ping result with regular expression
            match = re.search(r'(?P<rate>\d+)\% packet loss', result)
            success_rate = 100 - int(match.group('rate'))
            # log the success rate
            logger.info(banner('Ping {} with success rate of {}%'.format(
                                        destination,
                                        success_rate,
                                    )
                               )
                        )
