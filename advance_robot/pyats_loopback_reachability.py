
# import python
import re
import logging
from time import sleep

# import ats
from ats import aetest
from ats.log.utils import banner

# import genie
from genie.abstract import Lookup
from genie.utils.timeout import Timeout

# import genie.libs
from genie.libs import ops, conf, sdk, parser
from genie.libs.sdk.libs.utils.mapping import Mapping

# Genie Exceptions
from genie.harness.exceptions import GenieConfigReplaceWarning


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


# delete bgp neighbors
class DeleteBgpNeighbor(aetest.Testcase):
    '''Shut or Unshut the Learned BGP Neighbors'''

    @aetest.test
    def delete_bgp_neighbors(self, device, steps, testbed, number=1):
        '''Send configuration to unconfigure

           Args:
               uut (`obj`): Device object.
               abstract (`obj`): Abstract object.
               steps (`step obj`): aetest step object

           Returns:
               None

           Raises:
               pyATS Results
        '''
        # get device object
        device = testbed.devices[device]

        # create abstract object with genie packages
        self.parent.abstract = Lookup.from_device(device,
                                      packages={'sdk':sdk,
                                                'conf':conf,
                                                'ops':ops,
                                                'parser':parser})
        timeout = Timeout(max_time=60, interval=20)

        # update the number of removed neighbors
        self.mapping.num_values['neighbor'] = number

        # get bgp neighbors
        try:
            self.pre_snap = self.mapping.learn_ops(device=device,
                                                   abstract=self.parent.abstract,
                                                   steps=steps,
                                                   timeout = timeout)
        except Exception as e:
            self.errored("Section failed due to: '{e}'".format(e=e))

        for stp in steps.details:
            if stp.result.name == 'skipped':
                self.skipped('Cannot learn the feature', goto=['next_tc'])

        # save current device configurations
        self.parent.recover = self.parent.abstract.sdk.libs.abstracted_libs.restore.Restore()
        try:
            self.parent.recover.save_configuration(device, 'checkpoint', self.parent.abstract, default_dir=None)
        except Exception as e:
            self.failed('Saving the configuration failed', from_exception=e,
                        goto=['next_tc'])

        # unconfigure the bgp neighbors
        try:
            self.mapping.unconfigure(device=device, abstract=self.parent.abstract, steps=steps)
        except Exception as e:
            self.failed('Failed to unconfigure feature', from_exception=e)

        # sleep a little for router to respond
        sleep(5)

    mapping = Mapping(requirements={'ops.bgp.bgp.Bgp':{
                                          'requirements':[['info', 'instance', '(?P<instance>.*)', 'vrf', '(?P<vrf>.*)',
                                                           'neighbor', '(?P<neighbor>.*)', 'session_state', 'established'],
                                                          ['info', 'instance', '(?P<instance>.*)', 'bgp_id', '(?P<bgp_id>.*)']],
                                        'all_keys': True,
                                        'kwargs':{'attributes':['info']}}},
                      config_info={'conf.bgp.Bgp':{
                                     'requirements':[['device_attr', '{uut}', 'vrf_attr', '(?P<vrf>.*)',
                                                      'neighbor_attr','(?P<neighbor>.*)']],
                                     'verify_conf':False,
                                     'kwargs':{'mandatory':{'bgp_id': '(?P<bgp_id>.*)'}}}},
                      num_values={'vrf': 1, 'instance': 1, 'neighbor': 1})


class RestoreDevice(aetest.Testcase):
    '''Shut or Unshut the Learned BGP Neighbors'''

    @aetest.test
    def restore_device(self, device, testbed):
        # get device object
        device = testbed.devices[device]
        try:
            self.parent.recover.restore_configuration(device, 'checkpoint', self.parent.abstract)
        except GenieConfigReplaceWarning as e:
            self.passx('Configure replace requires device reload')
        except Exception as e:
            self.failed('Failed to restore the configuration', from_exception=e)