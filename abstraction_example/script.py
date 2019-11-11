'''
Abstraction demonstraction test-script. 

Run with:
    python script.py --testbed tb.yaml
    python script.py --testbed tb.yaml --release polaris_dev
    
Feel free to make changes to the tb.yaml file and see how lookup behavior change
'''

from genie import abstract

from ats import aetest

import abstracted_pkg

class CommonSetup(aetest.CommonSetup):
    
    @aetest.subsection
    def create_lookup_object(self, testbed, release, yang):
        for device in testbed.devices.values():            
            device.lib = genie.abstract.Lookup(device.os, device.type, release, yang)
            
class LookupTestcase(aetest.Testcase):
    
    @aetest.test
    def device_lookup(self, testbed):
        for name, device in sorted(testbed.devices.items()):
            
            print('operating on device: %s' % name)
            print('device os:', device.os)
            print('device type:', device.type)

            # lookup class
            obj = device.lib.abstracted_pkg.some_module.SomeClass()
            obj.some_method()
            
            # lookup function
            device.lib.abstracted_pkg.some_module.some_function()
            
            # lookup varibale
            print(device.lib.abstracted_pkg.some_module.some_var)
            
            print()
            
if __name__ == '__main__':
    
    import argparse
    from ats import topology
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', type = topology.loader.load)
    parser.add_argument('--release', type = str, default = None)
    parser.add_argument('--yang', action = 'store_true', default = None)
    
    args, _ = parser.parse_known_args()
    aetest.main(**vars(args))
