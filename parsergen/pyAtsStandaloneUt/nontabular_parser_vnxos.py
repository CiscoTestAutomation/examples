#!/bin/env python
import sys
from pprint import pprint
from textwrap import dedent
from collections import OrderedDict


python3 = sys.version_info >= (3,0)

if python3:
    from unittest.mock import Mock
    from unittest.mock import patch
else:
    from mock import Mock
    from mock import patch

ats_mock = Mock()
with patch.dict('sys.modules', 
        {'ats' : ats_mock}):
    from genie import parsergen
    from genie.parsergen import oper_fill

    from genie.parsergen.examples.parsergen.pyAts import parsergen_demo_mkpg


show_command_output_example  = '''\
show interface mgmt0
mgmt0 is up
admin state is up
  Hardware: Ethernet, address: 5254.0070.0dff (bia 5254.0070.0dff)
  Internet Address is 10.10.10.5/24
  MTU 1500 bytes, BW 0 Kbit, DLY 10 usec
  reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, medium is broadcast
  Port mode is routed
  auto-duplex, auto-speed
  Auto-Negotiation is turned on
  Auto-mdix is turned off
  EtherType is 0x0000 
  1 minute input rate 88 bits/sec, 0 packets/sec
  1 minute output rate 24 bits/sec, 0 packets/sec
  Rx
    254 input packets 6 unicast packets 245 multicast packets
    3 broadcast packets 82739 bytes
  Tx
    110 output packets 5 unicast packets 102 multicast packets
    3 broadcast packets 22698 bytes
'''

# Define how device stub will behave when accessed by production parser.
device_kwargs = {'is_connected.return_value':True, 
        'execute.return_value':dedent(show_command_output_example)}
dev1 = Mock(**device_kwargs)
dev1.name='router1'
dev_os = 'nxos'

attrValPairsToParse = [
    ('show.intf.if_name',                       'mgmt0'),
]

# Mock the call to determine the device's platform type
dev1.os = dev_os
pgfill = oper_fill (
    dev1,
    ('show_interface_<WORD>', [], {'ifname':'mgmt0'}),
    attrValPairsToParse,
    refresh_cache=True, regex_tag_fill_pattern='show\.intf',skip=True)
result = pgfill.parse()
print("\nThe following commands were just executed on the device : {}\n".
    format(dev1.execute.call_args))
pprint("Parsing result : {}".format(result))
if not result:
    pprint(str(pgfill))
#
# Print out keys in order of original registration.
# This can help debug marked-up text, since the parser gives up if
# it can't match a pattern.
#
dict_to_print = parsergen.ext_dictio[dev1.name]
sorted_output_dict = OrderedDict()
for key in parsergen._glb_regex_tags[dev_os]:
    if key in dict_to_print:
        sorted_output_dict[key] = dict_to_print[key]
pprint(list(sorted_output_dict.items()))


