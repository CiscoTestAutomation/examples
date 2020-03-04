import logging
from pyats import aetest
from genie.harness.base import Trigger

log = logging.getLogger()


class HelloWorld(Trigger):
    '''Just print Hello World'''

    @aetest.test
    def print_hello1(self, uut):
        '''Print Hello World'''
        log.info('Hello World')

    @aetest.test
    def print_hello2(self, uut):
        '''Why not do it again?'''
        log.info('Yes Yes, Hello World')

