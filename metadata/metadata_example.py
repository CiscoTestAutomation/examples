'''
This is a metadata script demonstrating how various data, eg, __version__, can 
be set by the engine.
'''

from pyats import aetest

__version__ = '99.99.0'

class CommonSetup(aetest.CommonSetup):
    
    @aetest.subsection
    def subsection_1(self, section):
        section.uid = 'subsection_one'
        
    @aetest.loop(var=[1,2,3])
    @aetest.subsection
    def subsection_2(self, section):
        pass
        
        
class TestcaseOne(aetest.Testcase):
    
    uid = 'testcase_one'
    name = 'an alternative name for testcase one'
    swversion = 'version string'
    hwversion = 'version string'
    fwversion = 'version string'
    tstversion = 'version string'
    
    @aetest.setup
    def setup(self):
        pass
        
    @aetest.test
    def test(self, section):
        section.uid = 'testcase_one_test'
        
@aetest.loop(var=[10,20,30])
class TestcaseTwo(aetest.Testcase):
        
    @aetest.setup
    def setup(self):
        pass
        
    @aetest.test
    def test(self, section):
        pass
        
