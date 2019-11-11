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
GigabitEthernet0/0 is up, line protocol is up 
  Hardware is iGbE, address is 5254.00f7.4fe8 (bia 5254.00f7.4fe8)
  Internet address is 10.10.10.2/24
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec, 
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full Duplex, 1Gbps, media type is RJ45
  output flow-control is unsupported, input flow-control is unsupported
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input 00:00:11, output 00:00:04, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     352 packets input, 113269 bytes, 0 no buffer
     Received 0 broadcasts (0 IP multicasts)
     0 runts, 0 giants, 0 throttles 
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 0 multicast, 0 pause input
     1982 packets output, 207638 bytes, 0 underruns
     0 output errors, 0 collisions, 2 interface resets
     12 unknown protocol drops
     0 babbles, 0 late collision, 0 deferred
     0 lost carrier, 0 no carrier, 0 pause output
     0 output buffer failures, 0 output buffers swapped out
'''

# Define how device stub will behave when accessed by production parser.
device_kwargs = {'is_connected.return_value':True, 
        'execute.return_value':dedent(show_command_output_example)}
dev1 = Mock(**device_kwargs)
dev1.name='router1'
dev_os = 'ios'

attrValPairsToParse = [
    ('show.intf.if_name',                       'GigabitEthernet0/0'),
]

# Mock the call to determine the device's platform type
dev1.os = dev_os
pgfill = oper_fill (
    dev1,
    ('show_interface_<WORD>', [], {'ifname':'GigabitEthernet0/0'}),
    attrValPairsToParse,
    refresh_cache=True, regex_tag_fill_pattern='show\.intf')
result = pgfill.parse()
print("\nThe following commands were just executed on the device : {}\n".
    format(dev1.execute.call_args))
pprint("Parsing result : {}".format(result))
if result:
    #
    # Parse succeeded.  Print out keys in order of original registration.
    # This can help debug marked-up text, since the parser gives up if
    # it can't match a pattern.
    #
    dict_to_print = parsergen.ext_dictio[dev1.name]
    sorted_output_dict = OrderedDict()
    for key in parsergen._glb_regex_tags[dev_os]:
        if key in dict_to_print:
            sorted_output_dict[key] = dict_to_print[key]
    pprint(list(sorted_output_dict.items()))
else:
    pprint(str(pgfill))


