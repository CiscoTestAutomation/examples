#!/bin/env python
import sys
from pprint import pprint
from textwrap import dedent


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
show interface MgmtEth0/0/CPU0/0
Wed Mar 11 18:19:28.909 EDT
MgmtEth0/0/CPU0/0 is up, line protocol is up 
  Interface state transitions: 1
  Hardware is Management Ethernet, address is 5254.00d6.36c9 (bia 5254.00d6.36c9)
  Internet address is 10.30.108.132/23
  MTU 1514 bytes, BW 0 Kbit
     reliability 255/255, txload Unknown, rxload Unknown
  Encapsulation ARPA,
  Duplex unknown, 0Kb/s, unknown, link type is autonegotiation
  output flow control is off, input flow control is off
  Carrier delay (up) is 10 msec
  loopback not set,
  ARP type ARPA, ARP timeout 04:00:00
  Last input 00:00:00, output 00:00:36
  Last clearing of "show interface" counters never
  5 minute input rate 84000 bits/sec, 33 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     17890219 packets input, 5613119704 bytes, 0 total input drops
     0 drops for unrecognized upper-level protocol
     Received 16015275 broadcast packets, 1792005 multicast packets
              0 runts, 0 giants, 0 throttles, 0 parity
     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
     15398 packets output, 1027241 bytes, 0 total output drops
     Output 4 broadcast packets, 0 multicast packets
     0 output errors, 0 underruns, 0 applique, 0 resets
     0 output buffer failures, 0 output buffers swapped out
     1 carrier transitions
'''

# Define how device stub will behave when accessed by production parser.
device_kwargs = {'is_connected.return_value':True, 
        'execute.return_value':dedent(show_command_output_example)}
dev1 = Mock(**device_kwargs)
dev1.name='router1'

attrValPairsToParse = [
    ('show.intf.if_name',                       'MgmtEth0/0/CPU0/0'),
]

# Mock the call to determine the device's platform type
dev1.os = 'iosxr'
pgfill = oper_fill (
    dev1,
    ('show_interface_<WORD>', [], {'ifname':'MgmtEth0/0/CPU0/0'}),
    attrValPairsToParse,
    refresh_cache=True, regex_tag_fill_pattern='show\.intf')
result = pgfill.parse()
print("\nThe following commands were just executed on the device : {}\n".
    format(dev1.execute.call_args))
pprint("Parsing result : {}".format(result))
if result:
    pprint(parsergen.ext_dictio[dev1.name])
else:
    pprint(str(pgfill))


