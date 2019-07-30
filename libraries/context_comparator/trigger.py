import time
import importlib

from ats import aetest
from genie.harness.base import Trigger
from genie.harness.base import Template
from genie.ops.base import Context

# Genie Libs
from genie.libs import parser
from genie.utils.diff import Diff

from genie.abstract import Lookup

default_exclude = ['maker', 'context_manager']


class Comparator(Trigger):

    @aetest.test
    def context1(self, uut, cmd, context1, section):
        '''Learn the first context'''
        section.id = 'context_{}'.format(context1)

        context = getattr(Context, context1)
        self.context1_ops = self._learn(uut, cmd, context)
        if not self.context1_ops.name:
            self.skipped("{} command is invalid or output is empty".\
                        format(context1), goto=['next_tc'])

    @aetest.test
    def context2(self, uut, cmd, context2, section):
        '''Learn the second context'''
        section.id = 'context_{}'.format(context2)

        context = getattr(Context, context2)
        try:
            self.context2_ops = self._learn(uut, cmd, context)
        except:
            self.failed("invalid {} command".format(context2), goto=['next_tc'])

    @aetest.test
    def compare(self, uut, cmd, context1, context2, exclude=[]):
        '''Compare between the two contexts'''
        exclude = default_exclude + exclude
        diff = Diff(self.context1_ops, self.context2_ops, exclude=exclude)
        diff.findDiff()

        # Verify that all keys are present
        if diff.diffs:
            self.failed("'{c1}' is not equal to '{c2}' for "
                        "command '{cmd}'\n{e}".format(c1=context1, c2=context2,
                                                      e=str(diff), cmd=cmd))

    def _learn(self, uut, cmd, context):
        '''Learn the specific show command via an Genie Ops object'''
        # Load the command
        
        kwargs = {} if 'parameters' not in cmd else cmd['parameters']
        cmd = self._load_pkg(uut, cmd)

        ops = Template(device=uut, cmd=cmd)
        # Set the right context
        ops.context_manager[cmd] = [context]

        # Learn the ops object
        ops.learn(**kwargs)
        return ops

    def _load_pkg(self, uut, cmd):
        '''Load the class and abstract it based on the device'''

        cls = cmd['class']
        pkg = cmd['pkg']
        mod = importlib.import_module(name=pkg)

        # Lookup is cached,  so only the first time will be slow
        # Otherwise it is fast
        lib = Lookup.from_device(uut, packages={pkg:mod})
        # Build the class to used to call
        keys = cls.split('.')
        keys.insert(0, pkg)
        for key in keys:
            lib = getattr(lib, key) 
        return lib


@aetest.subsection
def config_xml_version(self, testbed):
    '''Configure xml version to sync with current image'''

    # get uut
    devices = testbed.find_devices(aliases=['uut'])
    self.ver = {}

    # change the xml version to corresponding one.
    for uut in devices:
        lookup = Lookup.from_device(uut)
        version_obj = lookup.parser.show_platform.ShowVersion(device=uut)
        version_output = version_obj.parse()
        try:
            # terminal output xml 7.0.3.I7.3.
            # 7.0(3)I7(3) [build 7.0(3)I7(2.187)]
            ver = version_output['platform']['software']['system_version'].split()[0]
            ver = ver.replace('(', '.')
            ver = ver.replace(')', '.')
            if hasattr(uut, 'xml'):
                uut.xml.execute('terminal output xml {ver}'.format(ver=ver))
        except:
            pass