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



#
# Now, show how to use formatting to specify CLI commands:
#

print ("\n\n*** OS Agnostic CLI command formatting examples. ***\n\n")


# Define how device stub will behave when accessed by production parser.
device_kwargs = {'is_connected.return_value':True, 
        'execute.return_value':'dummy output'}
dev1 = Mock(**device_kwargs)

show_cmds = {
    'iosxr': {
        'SHOW_IP_INTF' : "show {=ipv4} interface {}",
        'SHOW_IP_INTF2': "show {=ipv4} interface {if-name}"
    },
    'nxos': {
        'SHOW_IP_INTF' : "show {=ip} interface {}",
        'SHOW_IP_INTF2': "show {=ip} interface {if-name}"
    }
}

regex = {
    'iosxr': {
        'dummy_regex_tag' : "dummy_regex"
    },
    'nxos': {
        'dummy_regex_tag' : "dummy_regex"
    }
}

parsergen.extend(show_cmds=show_cmds, regex_ext=regex)

# Mock the call to determine the device's platform type
dev1.name='router1'
dev1.os = 'iosxr'

args = ('SHOW_IP_INTF', [None, 'GigabitEthernet0/0/0/1'])
attrValPairsToParse = [('dummy_regex_tag','dummy_regex_value')]

pgfill = oper_fill (
    dev1,
    args,
    attrValPairsToParse,
    refresh_cache=True)
result = pgfill.parse()



print("Using a positional argument to specify the CLI command:")
print("The following commands were just executed on the XR device : {}".
    format(dev1.execute.call_args))

# Clear our the mock device's call_args.
dev1.execute.reset_mock()

# Redefine the platform type of the mocked device
dev1.name='router2'
dev1.os = 'nxos'

pgfill = oper_fill (
    dev1,
    args,
    attrValPairsToParse,
    refresh_cache=True)
result = pgfill.parse()

print("\n\n")
print("Using a positional argument to specify the CLI command:")
print("The following commands were just executed on the NXOS device : {}".
    format(dev1.execute.call_args))


print("\n\n")

# Clear our the mock device's call_args.
dev1.execute.reset_mock()

# Redefine the platform type of the mocked device
dev1.name='router1'
dev1.os = 'iosxr'

args = ['SHOW_IP_INTF2', [], {'if-name' : 'GigabitEthernet0/0/0/1'}]

pgfill = oper_fill (
    dev1,
    args,
    attrValPairsToParse,
    refresh_cache=True)
result = pgfill.parse()

print("Using a keyword argument to specify the CLI command:")
print("The following commands were just executed on the XR device : {}".
    format(dev1.execute.call_args))

# Clear our the mock device's call_args.
dev1.execute.reset_mock()

# Redefine the platform type of the mocked device
dev1.name='router2'
dev1.os = 'nxos'

pgfill = oper_fill (
    dev1,
    args,
    attrValPairsToParse,
    refresh_cache=True)
result = pgfill.parse()

print("\n\n")
print("Using a positional argument to specify the CLI command:")
print("The following commands were just executed on the NXOS device : {}".
    format(dev1.execute.call_args))




