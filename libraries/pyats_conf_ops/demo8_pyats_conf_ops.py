#!/bin/env python
###################################################################
# Genie - XR - XE - Cli - Yang
###################################################################

import time
import logging

# Needed for aetest script
from ats import aetest
from ats.utils.objects import R
from ats.datastructures.logic import Not

from genie.abstract import Lookup
from genie.libs import conf, ops

# Import Genie infra
from genie.conf import Genie
from genie.libs.conf import interface
from genie.libs.conf.ospf.ospf import Ospf
from genie.libs.conf.vrf.vrf import Vrf
from genie.libs.conf.address_family import AddressFamily,\
     AddressFamilySubAttributes

log = logging.getLogger()

###################################################################
###                  COMMON SETUP SECTION                       ###
###################################################################

class common_setup(aetest.CommonSetup):
    '''Connect, Configure, and Verify the configuration was
       applied correctly
    '''

    @aetest.subsection
    def genie_init(self, testscript, testbed, uut_alias, helper_alias,
                   steps, context):
        """ Initialize the environment """

        with steps.start('Initializing the environment for'
                         ' Genie Configurable Objects'):

            # Context to mention which Commnand type to use. (Cli/Yang)
            # It has to be set before the Genie convertion, as the right
            # Interface has to be instantiated.
            # The default value is 'cli', so only do it in the 'yang' case
            if context == 'yang':
                # Set all device to yang
                # Or, only specific device could be set to use 'yang', and the
                # rest use 'cli'
                for dev in testbed.devices.values():
                    dev.context ='yang'

            # Initialize Genie Testbed
            # It also sets the variable 'Genie.testbed', to hold the testbed
            Genie.init(testbed=testbed)

            # Test script parameters are added so
            # these can be passed on to the subsections.
            uut = Genie.testbed.find_devices(aliases=[uut_alias])[0]
            helper = Genie.testbed.find_devices(aliases=[helper_alias])[0]
            testscript.parameters['uut'] = uut
            testscript.parameters['helper'] = helper

            # Overwrite the pyATS testbed for Genie Testbed
            testscript.parameters['testbed'] = Genie.testbed

            # area_id from the datafile
            testscript.parameters['area_id'] = self.area_id

            # Mark testcase with looping information
            aetest.loop.mark(ping, device=[uut, helper])

    @aetest.subsection
    def connect(self, testbed, testscript, steps, context, pool_num):
        '''Connect to the devices, using either Cli and/or Yang'''

        # Connect to all the devices
        with steps.start('Connect to all devices'):
            for dev in testbed.devices.values():
                # If the context of this device is Yang, then connect via Yang
                if dev.context == 'yang':
                    time.sleep(5)
                    dev.connect(alias = 'nc', via = 'netconf')
                    # As the alias name can be anything, We need to tell the
                    # infrastructure what is the alias of the yang connection
                    dev.mapping['yang'] = 'nc'

                    time.sleep(5)

                # Cli supports a pool device mechanism. This will allow Ops
                # to learn the features faster.
                if pool_num > 1:
                    dev.start_pool(alias='vty', via='cli', size=pool_num)
                else:
                    dev.connect(via='a', alias='cli')
                # As the alias name can be anything, We need to tell the
                # infrastructure what is the alias of the cli connection
                # Use connection a for cli communication to the device
                dev.mapping['cli'] = 'a'

                # Abstraction
                # Right now abstraction is done via OS and Context.
                dev.lib = Lookup(dev.os, dev.context, packages={'conf':conf, 'ops':ops})


    @aetest.subsection
    def configure_basic_ospf(self, testbed, testscript, uut, helper, steps):
        '''Configure Ospf'''

        # To configure Ospf, we are doing the following:
        #
        # We want to configure it on two devices interconnected, so we are
        # asking to find us a link which reach the 'uut' and the 'helper'
        # device.
        #
        # Then we create a 'Ospf' Object with a name (to represent the Ospf
        # name) and add this Ospf to the link. We configure the Ospf object
        # with area_id
        #
        # Lastly, we want to configure an ip address on the interface of this
        # link, and do a 'no shut'. This is done with Genie ipv4 and ipv6
        # generator
        #
        # And we configure each interface and the Ospf.

        with steps.start('Find a link between uut and helper device and '
                         'configure ospf process id {pro} on '
                         'it'.format(pro=self.ospf_1)):
            # Using the find api
            # Find a link that has an interface attached to device uut
            # and helper device. These interace must be of type ethernet.
            link = testbed.find_links(R(interfaces__device__name=uut.name),
                                      R(interfaces__device__name=helper.name),
                                      R(interfaces__type='ethernet'),
                                      count=1)[0]

        # Take this link and configure Ospf on it
        with steps.start('Configure ospf process id {pro} on '
                         'the link'.format(pro=self.ospf_1)):
            # Create Ospf instance
            ospf = Ospf()
            ospf.instance = self.ospf_1
            ospf.feature_ospf = True

            # Adding ospf feature to the link
            link.add_feature(ospf)

            # Adding area to the vrf attribute
            ospf.device_attr[uut].vrf_attr[None].area_attr[self.area_id]
            ospf.device_attr[helper].vrf_attr[None].area_attr[self.area_id]

            # Initiating ipv4 and ipv6 addresses
            ipv4s = []
            ipv6s = []

        with steps.start('Building the interface configuration'):
            # Generate ipv4 and ipv6 addresses, depending on the length of the
            # interfaces
            ipv4rng = iter(testbed.ipv4_cache.reserve(count=len(link.interfaces)))
            ipv6rng = iter(testbed.ipv6_cache.reserve(count=len(link.interfaces)))
            for intf in link.interfaces:
                # Configuring the interface with its attribute
                intf.shutdown = False
                intf.layer = interface.Layer.L3

                # Assigning Ipv4 and ipv6 addresses to the intervace
                intf.ipv4 = next(ipv4rng)
                ipv4s.append(intf.ipv4.ip)
                intf.ipv6 = next(ipv6rng)
                ipv6s.append(intf.ipv6.ip)

                # Adding interface to the area attribute
                ospf.device_attr[intf.device].vrf_attr[None]\
                                .area_attr[self.area_id].interface_attr[intf].if_admin_control = True

                # Build interface config and apply it to the device
                intf.build_config()

        with steps.start('Building the ospf configuration'):
            # Configure Ospf on all 'uut' and 'helper'
            ospf.build_config()

        # Using parameters to pass around the link and the ospf object.
        testscript.parameters['link_1'] = link
        testscript.parameters['ospf_1'] = ospf

    def interface_up(self, ospf, ospf_name, vrf_name, area, dev_intf,
                     intf1_loop=None):
        '''Method for verifying if the interface is up

           Return none if the states are the one is expected
           Raise an exception if the states are not the one expected
        '''

        try:
            interfaces = ospf.info['vrf'][vrf_name]['address_family']['ipv4']['instance'][ospf_name]['areas'][area]['interfaces']
        except KeyError:
            return

        for intf in interfaces.values():
            assert intf['enable'] == True

    @aetest.subsection
    def verify_basic_ospf(self, uut, helper, steps, link_1):
       '''Verify if the basic configuration of Ospf was done correctly'''

       # Verify for both device
       for dev in [uut, helper]:

           # Find the interface of this device, and the neighbor one
           dev_intf = link_1.find_interfaces(device=dev)[0]
           # TODO - Bug here
           neighbor_intf = link_1.find_interfaces(device=Not(str(dev)))[0]

           # Create an instance of Ospf Ops object for a particular device
           ospf = dev.lib.ops.ospf.ospf.Ospf(device=dev)

           # Ops objects have a builtin polling mechanism to learn a feature.
           # It will try 20 times to learn the feature, with sleep of 10 in
           # between and to verify if it was learnt correctly, will call the
           # verify function. If this function does not raise an exception,
           # then will assume it was learnt correctly.
           try:
               ospf.learn_poll(verify=self.interface_up, sleep=10, attempt=10,
                               ospf_name=self.ospf_1, vrf_name='default',
                               area=self.area_id, dev_intf=dev_intf)
           except StopIteration as e:
               self.failed(str(e))

       log.info("Configuration was applied correctly")

    @aetest.subsection
    def configure_ospf(self, testbed, testscript, uut, helper, steps):
        '''Configure a bigger Ospf configuration'''

        # To configure Ospf, we are doing the following:
        #
        # We want to configure it on two devices interconnected, so we are
        # asking to find us a link which reach the 'uut' and the 'helper'
        # device. We are taking the second ones, as the first one was used
        # for the previous subsection.
        #
        # Then we create a 'Ospf' Object with a name (to represent the Ospf
        # name) and add this Ospf to the link, and add configuration to it.
        #
        # Then we create a 'Vrf' object, which is added to the vrf.
        #
        # Lastly, we want to configure an ip address on the interface of this
        # link, and do a 'no shut'. This is done with Genie ipv4 and ipv6
        # generator. It is also done for the loopback interfaces.
        #
        # And we configure each interface, the vrf and the Ospf.

        with steps.start('Find a link between uut and helper device and '
                         'configure ospf with '
                         'pid {pro} on it'.format(pro=self.ospf_2)):
            link = testbed.find_links(R(interfaces__device__name=uut.name),
                                      R(interfaces__device__name=helper.name),
                                      R(interfaces__type='ethernet'))

        # We are taking the second link
        link = link[1]

        # passing this link to testscript parameters
        # so we can be used in other subsections
        testscript.parameters['link_2'] = link

        with steps.start('Find a loopback link between uut and helper device '
                         'and configure ospf with pid 200 on it'):
            loopback_link = testbed.find_links\
                            (R(interfaces__device__name=uut.name),
                             R(interfaces__device__name=helper.name),
                             R(interfaces__type = 'loopback'),count=1)[0]

        # Take this link and configure Ospf on it
        with steps.start('Configure ospf with pid {pro} on the '
                         'link'.format(pro=self.ospf_2)):

            # Create a ospf object
            ospf = Ospf(ospf_name=self.ospf_2)
            ospf.instance = self.ospf_2

            # Adding ospf to the link and loopback_link
            link.add_feature(ospf)
            loopback_link.add_feature(ospf)

            # Add attributes to the ospf object
            ospf.log_adjacency_changes = self.log_adjacency_changes
            ospf.nsf = self.nsf
            ospf.nsr = self.nsr
            ospf.auto_cost_ref_bw = self.auto_cost_ref_bw

        with steps.start("Configure vrf '{vrf}' under "
                         "ospf process id {pro} on "
                         "the link".format(pro=self.ospf_2,
                                           vrf=self.vrf_name)):

            # Create vrf Object
            vrf = Vrf(name=self.vrf_name)

            # Add the address_family attributes to vrf
            vrf.device_attr[uut].address_family_attr['ipv4 unicast']
            vrf.device_attr[helper].address_family_attr['ipv4 unicast']
            vrf.device_attr[uut].address_family_attr['ipv6 unicast']
            vrf.device_attr[helper].address_family_attr['ipv6 unicast']

            # Adding area to the vrf attribute
            ospf.device_attr[uut].vrf_attr[vrf].area_attr[self.area_id]
            ospf.device_attr[helper].vrf_attr[vrf].area_attr[self.area_id]
            for dev in testbed.devices.values():
                dev.add_feature(vrf)
                vrf.device_attr[dev].build_config()

        with steps.start('Building the interface configuration with Ospf '
                         'process id {pro}'.format(pro=self.ospf_2)):

            # Initiating ipv4 and ipv6 addresses
            ipv4s = []
            ipv6s = []

            # Generate ipv4 and ipv6 addresses, depending on the length of the
            # interfaces
            ipv4rng = iter(testbed.ipv4_cache.reserve(count=len(link.interfaces)))
            ipv6rng = iter(testbed.ipv6_cache.reserve(count=len(link.interfaces)))
            for intf in link.interfaces:
                # Adding vrf to the interface
                intf.vrf = vrf

                # Configuring interface with its attributes
                intf.shutdown = False
                intf.layer = interface.Layer.L3

                # Assigning Ipv4 and ipv6 addresses to the interface
                intf.ipv4 = next(ipv4rng)
                ipv4s.append(intf.ipv4.ip)
                intf.ipv6 = next(ipv6rng)
                ipv6s.append(intf.ipv6.ip)

                # Adding interface to the area attribute
                ospf.device_attr[intf.device].vrf_attr[vrf]\
                                .area_attr[self.area_id].interface_attr[intf].if_admin_control = True

                # Build interface config and apply it to the device
                intf.build_config()

        with steps.start('Building the loopback interface configuration with '
                         'Ospf process id {pro}'.format(pro=self.ospf_2)):

            for intf in loopback_link.interfaces:
                # Add vrf to the loopback interface object
                intf.vrf = vrf
                intf.layer = interface.Layer.L3

                # Assigning ipv4 and ipv6 addresses to the loopback interface
                intf.ipv4 = testbed.ipv4_cache.reserve(prefixlen=32)[0]
                ipv4s.append(intf.ipv4.ip)
                intf.ipv6 = testbed.ipv6_cache.reserve(prefixlen=128)[0]
                ipv6s.append(intf.ipv6.ip)

                # Adding the Loopback interface to the ospf object
                ospf.device_attr[intf.device].vrf_attr[vrf]\
                                 .area_attr[self.area_id].interface_attr[intf].if_admin_control = True

                # Assigning the Loopback address as the OSPF router-id
                if intf.device.name == uut.name :
                    ospf.device_attr[uut].vrf_attr[vrf]\
                        .router_id = intf.ipv4.ip.exploded
                elif intf.device.name == helper.name:
                    ospf.device_attr[helper].vrf_attr[vrf]\
                        .router_id = intf.ipv4.ip.exploded

                # Building loopback interface configuration
                intf.build_config()

        with steps.start('Building the ospf configuration with '
                         'Ospf process id {pro}'.format(pro=self.ospf_2)):
            # Building OSPF configuration
            ospf.build_config()

        # adding vrf, ospf and loopback to parameters
        testscript.parameters['vrf'] = vrf
        testscript.parameters['ospf'] = ospf
        testscript.parameters['loopback_link_2'] = loopback_link

        # Adding information for the ping test
        aetest.loop.mark(ping.test, destination=ipv4s,
                         vrf=[vrf.name]*(len(link.interfaces) +
                         len(loopback_link.interfaces)))

    @aetest.subsection
    def verify_ospf(self, uut, helper, steps, link_2, loopback_link_2):
       '''Verify if the Ospf configuration was done correctly'''

       # Verify for both device
       for dev in [uut, helper]:
           # Find the interface of this device
           dev_intf = link_2.find_interfaces(device=dev)[0]
           neighbor_intf = link_2.find_interfaces(device=Not(str(dev)))[0]

           # Same for loopback
           intf1_loop = loopback_link_2.find_interfaces(device=dev)[0]
           intf2_loop = loopback_link_2.find_interfaces(device=Not(str(dev)))[0]
           ospf = dev.lib.ops.ospf.ospf.Ospf(device=dev)
           try:
               ospf.learn_poll(verify=self.interface_up, sleep=10, attempt=10,
                               ospf_name=self.ospf_2, vrf_name=self.vrf_name,
                               area=self.area_id, dev_intf=dev_intf,
                               intf1_loop=intf1_loop)
           except StopIteration as e:
               self.failed(str(e))

       time.sleep(60)
       log.info("Configuration was applied correctly")

##################################################################
##                     TESTCASES SECTION                       ###
##################################################################
class ping(aetest.Testcase):
    """This is user Testcases section"""

    @aetest.test
    def test(self, device, destination, vrf, steps):
        with steps.start('Ipv4 Ping Test from {dev} to {ip}'.
                         format(dev=device.name,ip=destination)):
            """Ping an ip"""
            log.info("{dev} pings {ip}".format(dev=device.name, ip=destination))
            device.ping(destination, vrf=vrf, interval=1000, count=30)

class Modify(aetest.Testcase):
    """Modify configuration"""

    @aetest.test
    def test(self, ospf, uut, vrf, steps):
        """Modify ospf attribtue"""

        # Modify auto cost reference bandwidth to 10
        with steps.start('Modify auto-cost reference bandwidth'
                         ' attribute on '
                         'ospf process-id {pro} vrf {vrf}'
                         .format(vrf=vrf.name, pro=self.ospf_2)):

            # Modify the value auto_cost_ref_bw
            ospf.device_attr[uut].auto_cost_ref_bw = self.auto_cost_ref_bw
            ospf.build_config(attributes={'device_attr':{uut:{'vrf_attr':{'*':{'auto_cost_ref_bw':None}}}}})


#####################################################################
####                       COMMON CLEANUP SECTION                 ###
#####################################################################

class common_cleanup(aetest.CommonCleanup):
    """ Common Cleanup for Sample Test """

    @aetest.subsection
    def clean_everything(self, steps):
        testbed = Genie.testbed
        """ Common Cleanup Subsection """
        with steps.start('Unconfig testbed'):
            if testbed:
                log.info("Aetest Common Cleanup ")

                # Unconfigure the whole testbed
                # (ie) unconfigure the link, devices and the feature
                testbed.build_unconfig()
