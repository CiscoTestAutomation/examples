import pprint
import logging
from pyats import aetest
from genie.harness.base import Trigger

log = logging.getLogger()


class Basic(Trigger):
    '''Just print Hello World'''

    @aetest.test
    def parse_example(self, uut):
        '''Parse example'''
        output = uut.parse('show version')
        # Output now contains a dictionary, you can do any logic you want here
        log.info('The dictionary returned by show version is:\n{}'.format(output))

        # The following device action can be used
        # device.parse('show version') <-- Call a parser and returns a dictionary datastructure
        # device.execute('show version') <-- Send command to the device and return string from the device
        # device.configure('interface ethernet2/2\nshutdown') <-- Go to conf t and send configuration to the device
        # device.api.get_interface_mtu_size('Ethernet2/2') <-- Call any of our apis 
        # device.learn('bgp') <-- OS Agnostic model for specific feature. The object returned has a .info which gi    ves a dictionary which is identical between all OS.

    @aetest.test
    def execute_example(self, uut):
        '''Why not do it again?'''
        output = uut.execute('show clock')
        # Output now contains the string which was returned by the device
        log.info('The string returned by show clock is:\n{}'.format(pprint.pprint(output)))

