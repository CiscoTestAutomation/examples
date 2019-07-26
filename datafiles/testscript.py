#!/usr/bin/env python
'''
This is a very short script intended to help the user undersand what datafiles
are, how to use them & how datafiles affect your script's normal execution.

First, run this script by itself:
    bash$ python testscript.py

Now, add datafile:
    bash$ python testscript.py -datafile data/simple_data.yaml

Then, try extended datafile:
    bash$ python testscript.py -datafile data/extended_data.yaml
'''

import logging

from pyats import aetest

logger = logging.getLogger(__name__)

parameters = {
    'script_param_a': 'default_value_a',
    'script_param_b': 'default_value_b',
}

module_var_a = 'module var a value'

class CommonSetup(aetest.CommonSetup):

    parameters = {
        'cc_param_a': 1,
        'cc_param_b': 2, 
    }

    @aetest.subsection
    def common_setup_params(self, cc_param_a, cc_param_b):
        logger.info('the following parameters are local to common_setup')
        logger.info('  cc_param_a = %s' % cc_param_a)
        logger.info('  cc_param_b = %s' % cc_param_b)

class MyTestcase(aetest.Testcase):

    parameters = {
        'tc_param_a': 100,
        'tc_param_b': 200, 
    }

    class_var_a = 'class var a value'

    @aetest.test
    def uid_and_groups(self):
        logger.info('notice how testcase uid/groups are modified')
        logger.info('  uid = %s' % self.uid)
        logger.info('  groups = %s' % self.groups)

    @aetest.test
    def script_params(self, script_param_a, script_param_b):
        logger.info('the following parameters are script-level')
        logger.info('  script_param_a = %s' % script_param_a)
        logger.info('  script_param_b = %s' % script_param_b)

    @aetest.test
    def testcase_params(self, tc_param_a, tc_param_b):
        logger.info('the following parameters are local to this testcase')
        logger.info('  tc_param_a = %s' % tc_param_a)
        logger.info('  tc_param_b = %s' % tc_param_b)

    @aetest.test
    def module_variables(self):
        logger.info('the following variables are defined at module level')
        logger.info('  module_var_a = %s' % module_var_a)
        logger.info('  module_var_b = %s' % module_var_b)

    @aetest.test
    def class_attributes(self):
        logger.info('the following attributes are defined at class level')
        logger.info('  class_var_a = %s' % self.class_var_a)
        logger.info('  class_var_b = %s' % self.class_var_b)


if __name__ == '__main__': # pragma: no cover
    logging.root.setLevel(logging.INFO)
    aetest.main()
