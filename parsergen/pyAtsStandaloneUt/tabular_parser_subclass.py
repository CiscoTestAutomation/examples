#!/bin/env python
import sys
from pprint import pprint

python3 = sys.version_info >= (3,0)

if python3:
    from unittest.mock import Mock
    from unittest.mock import patch
else:
    from mock import Mock
    from mock import patch

ats_mock = Mock()
with patch.dict('sys.modules', {'ats' : ats_mock}):
    from genie import parsergen
    from genie.parsergen import oper_fill_tabular


third_show_command_output_example  = '''
RP/0/0/CPU0:iox#show isis database
Wed Dec 16 09:48:55.017 EST

IS-IS ring (Level-1) Link State Database
LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime  ATT/P/OL
iox.00-00           * 0x00000008   0xf9fd        1003            0/0/0
ioxbfd.00-00          0x00000004   0x8f36        862             0/0/0

Total Level-1 LSP count: 4     Local Level-1 LSP count: 1

IS-IS ring (Level-2) Link State Database
LSPID                 LSP Seq Num  LSP Checksum  LSP Holdtime  ATT/P/OL
iox.00-00           * 0x00000009   0x351a        1003            0/0/0
iox.01-00             0x00000002   0x0ead        922             0/0/0

Total Level-2 LSP count: 4     Local Level-2 LSP count: 1
'''

def _hexint (val):
    return int(val, 16)

def cleanupLspId (field):
    return field


class my_isis_database_column_parser_t (oper_fill_tabular):
    field_mapping = {
        'LSPID'       :   str,   
        'LSP Seq Num' :   _hexint,
        'LSP Checksum':   _hexint,
        'LSP Holdtime':   None,
        }

    table_title_mapping = [ int ]

    def __init__ (self, device, show_command):
        headers = ["LSPID", "LSP Seq Num", "LSP Checksum", 
        "LSP Holdtime",  "ATT/P/OL"]
        labels = headers

        super(my_isis_database_column_parser_t, self).__init__(
         device,
         show_command,
         header_fields=headers,
         table_terminal_pattern="Total Level-[12] LSP count:",
         table_title_pattern = 
         r"IS-IS (?:[-\w]+ )?\(?Level-([12])\)? Link State Database:?",
         label_fields = labels)

    def cleanup_entry_field (self, header, field):
        if header == "LSPID":
            # Strip the "*" off the LSPID for the router's own LSPID.
            return cleanupLspId(field)
        else:
            return field


# Define how device stub will behave when accessed by production parser.
device_kwargs = {'is_connected.return_value':True, 
        'execute.return_value':third_show_command_output_example}
dev1 = Mock(**device_kwargs)

result = my_isis_database_column_parser_t(dev1, "show isis database")

print("\nThe following commands were just executed on the device : {}\n".
    format(dev1.execute.call_args))

if result.entries[2]['iox.01-00']['LSP Holdtime'] == '922':
    print ("Test passed")
    pprint(result.entries)
else:
    print ("Test failed")

