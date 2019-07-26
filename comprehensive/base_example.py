#!/usr/bin/env python

'''base_example.py

This is a comprehensive example base script that walks users through pyATS
infrastructure features, what they are for, how they are used, how it impacts
their testing, etc.

This is called the 'base' script: it provides the groundwork for other test
scripts within this directory to inherit from it and extend it further, creating
multiple variant scripts from here onwards. For example:
    - base script: feature_x_sanity.py
    - variant 1  : feature_x_regression.py
    - variant 2  : feature_x_scalability.py
    - variant 3  : feature_x_ha_traffic.py
    - etc...

The idea is simple: leverage python inheritance and create testscripts inherting
from each other, reducing the overall code base by increasing code depth &
re-useability.

Note:
   Any comments with "#*" in front of them (like this entire comment box) are
   for example/infrastructure clarifications only.

Warning:
   This testscript contains direct testcase definitions in favour of a more
   fluidic learning experience, demonstration content/features linearly. This
   is not standard testscript design.
   In your actual testscripts, testcases shall be defined in testcases/ module,
   and your main scripts should be only using testcases inheritances & defining
   testcase data.

Author:
   Siming Yuan, Cisco Systems Inc.

Support:
   pyats-support-ext@cisco.com

Arguments:
    This script requires two script arguments (argument_A and argument_B) to be
    passed in from the job file for demonstration purposes.

    argument_A: an argument
    argument_B: another argument

Examples:
    # to run under standalone execution
    bash$ python base_example.py

    # to run with datafile under command-line
    bash$ python base_example.py -datafile=data/base_datafile.yaml

    # to run under easypy
    bash$ pyats run job job/example_job.py

'''

#
# optional author information
#
__author__ = 'Cisco Systems Inc.'
__copyright__ = 'Copyright (c) 2019, Cisco Systems Inc.'
__contact__ = ['pyats-support-ext@cisco.com']
__date__= 'March 16, 2019'
__version__ = 2.0

#
# import statements
#
import logging
import argparse

from pyats import aetest
from pyats.log.utils import banner

# import local library
from libs import local_library

# create a logger for this module
logger = logging.getLogger(__name__)

#*******************************************************************************
#* TESTSCRIPT PARAMETERS
#*
#*  testscripts are driven by data. These data are called 'parameters' within
#*  pyATS scripts. Parameters follows a predefined inheritance rule:
#*      - child section parameters inherits parent section parameters.
#*
#*  this relationship can be charted as (<- denoting parent of):
#*
#*      TestScript <- CommonSetup   <- Subsections
#*           \---- <- Testcase      <- Setup/Test/Cleanup
#*            `--- <- CommonCleanup <- Subsections
#*
#*  or, in set theory, using TestScript/CommonSetup/Subsection as example:
#*          +----------------------------------------------+
#*          | +-----------------------------+  Subsections |
#*          | | +------------+  CommonSetup |   parameters |
#*          | | | TestScript |   parameters |              |
#*          | | | parameters |              |              |
#*          | | +------------+              |              |
#*          | +-----------------------------+              |
#*          +----------------------------------------------+
#*
#*  to define TestScript parameter defaults, create a dictionary named
#* 'parameters' directly within your testscript.
#*      parameters = {
#*          <keys>: <values>,
#*      }
#*
#*  if this testscript was called with script arguments (provided to script),
#*  these script arguments are updated into this TestScript parameter
#*  dictionary (overwriting any conflicting ones).
#*******************************************************************************

#
# testscript default parameters
#
parameters = {
    # defining some testscript parameter defaults
    'parameter_A': 'value A',
    'parameter_B': 'value B',
}

#*******************************************************************************
#* COMMON SETUP SECTION
#*
class CommonSetup(aetest.CommonSetup):
    '''Common Setup Section

    This is the docstring for your common setup section. Users should document
    the number of common setup subsections so that by reading this block of
    comments, it gives a generic feeling as to how CommonSetup is built and run.
    Below is an example of subsection breakdowns.

    Users may have an arbitrary number of subsections with arbitrary (hopefully
    meaningful) names.

    Common Setup section is optional in a testscripts. If defined, its report
    UID is always 'common_setup'.

    Subsections:
        a_simple_subsection: the simpletest subsections
        using_parameters: subsection demonstrating the use of parameters
        results_default_to_passed: demonstrating that result defaults.
        assertion_error_is_failed: demonstrating AssertionError -> Failed
        exception_driven_behavior_error: demonstrating Exception -> Errored
        self_is_self: in TestContainers, self is always self.

    Usages:
        - to define a CommonSetup section, create a class that inherits
          aetest.CommonSetup class
        - use @aetest.subsection decorator to mark methods in the CommonSetup
          as a subsection. The name of the function will be used as the
          subsection ID.

    Sequence:
        - CommonSetup section is always run first in a test script.
        - unless otherwise specified, subsections run after each other in the
          same sequence as defined in this file.
        - in the case of inheritance, the parent class's subsections runs first.

    Behavior:
        - each test script may have only one CommonSetup section, and must be
          further broken down into subsections
        - subsections are independent: each subsection will run regardless of
          the previous subsection's results.
        - CommonSetup counts as 1 section ran in the final number of executed
          section counts.

    Results:
        - the overall result of Common Setup section is calculated as the roll
          up of all its subsection's results. Result roll up behavior is well
          documented with pyats.results module.

    '''

    #******************************
    #* Simple Subsection
    #*
    #*  defining the most simplistic subsections.
    #*
    #*  subsection sare defined by applying the @aetest.subsection decorator
    #*  to a method. This marks it as a subsection. The function name is used
    #*  as the subsection uid/name.
    @aetest.subsection
    def a_simple_subsection(self):
        '''A Simple Subsection

        Use this docstring section to describe what is being done in this
        subsection.

        Note:
            this subsection is empty and doing just about nothing. probably not
            a good idea to submit to code reviews, sanity/regression.
        '''

        #******************************
        #* Results
        #*
        #*   if sections are not provided any results directly, the following
        #*   behavior takes place:
        #*      - if the section ran in full without issues, it is Passed.
        #*      - if an AssertionError is caught, it is Failed
        #*      - if any other Exceptions are caught, it is Errored
        #*
        #*   You can also directly provide results to each section using the
        #*   following result methods:
        #*          self.passed()
        #*          self.failed()
        #*          self.errored()
        #*          self.skipped()
        #*          self.blocked()
        #*          self.aborted()
        #*          self.passx()
        #*
        #*      each of the above apis also allows a reason to be provided:
        #*          self.failed('because I needed to fail :(')
        #*
        #*      and allows a goto option to redirect the next call
        #*          self.failed(reason='just cuz', goto='common_cleanup')
        #*
        #* Note:
        #*   when result for a section is provided, the section execution
        #*   immediately halts, returns, and the engine will continue running
        #*   the next section in line. Thus, section results can only be
        #*   provided once.

        # storing a value in self (to be used later)
        self.value_stored_from_simple_subsection = 'awesome'

        # let's provide a result and a msg
        self.passed('my example subsection is so awesome it always passes!')

        # the following code is simply never excuted
        logger.info('I am never executed :-(')

    #******************************
    #* CommonSetup Results
    #*
    #*  if common_setup result is not Passed, Skipped or Passx, all testcases
    #*  will be blocked. Thus, in order keep executing the remaining testcases
    #*
    #*  due to this constrait, result behavior subsections are located in
    #*  CommonCleanup.

    #******************************
    #* Using Script Parameters
    #*
    #*  keep in mind that script input argument becomes testscript base
    #*  parameters, and thus inherited by CommonSetup as parameters, described
    #*  in the testscript parameters section above.
    #*
    #*  all parameters are:
    #*      - accessible as self.parameters, and,
    #*      - useable as section function arguments.
    #*
    #*  if parameters are used as function arguments, their corresponding
    #*  parameter values will be provided as inputs.
    @aetest.subsection
    def using_parameters(self, testbed, parameter_A, parameter_B):
        '''Demonstrating how to use parameters

        When this section is run, these parameters will be passed in by the
        test engine. If a referenced parameter doesn't exist, an exception is
        raised.

        Parameters:
            testbed: this is the testbed parameter. 'testbed' parameter
                     is provided to testscript automatically if Easypy
                     is launched with --testbed-file argument.
            parameter_A/B: custom parameters serving as examples.
        '''

        # log some information
        # note that parameter_A/B were set in the testscript parameters
        # and thus propagates to this common_setup subsection
        logger.info('testbed: %s' % testbed)
        logger.info('Parameter A: %s' % parameter_A)
        logger.info('Parameter B: %s' % parameter_B)


    #******************************
    #* TestContainer Consistency
    #*
    #*  self within the same TestContainer always refers to the same object
    #*  instance. CommonSetup is an object, and each subsection is simply a
    #*  bound class instance method. During execution, all subsection methods
    #*  are passed the same CommonSetup object instance, and thus passing
    #*  values around subsection can be done easily using object attributes.
    #*
    #*  WARNING:
    #*     This is significantly different from Python unittest, where each
    #*     test method is instantiated and encapsulated in its own test class.
    @aetest.subsection
    def self_is_self(self):
        '''Self is always self within the same section

        reading and assessing a value set in previous subsection.
        '''

        # acces a value stored from a_simple_subsection:
        assert self.value_stored_from_simple_subsection is 'awesome'

    #******************************
    #* Looping Subsections
    #*
    #*  subsections can be looped. Loop subsections by using the @aetest.loop
    #*  decorator and providing it some loop parameters. Each loop iteration
    #*  of this subsection is considered a unique, separate section (as if it
    #*  was actually defined multiple times.)
    #*  for this demo, we'll be using subsection.loop shortcut
    @aetest.subsection.loop(result = ['passed', 'skipped'])
    def subsection_looped_with_parameter(self, result):
        '''subsection_looped_with_parameter

        This subsection will be looped 2 times, each time giving a result
        provided by the results parameter.
        '''

        # call the result api based on result parameter input
        # equivalent to self.passed(), self.skipped()
        result_api = getattr(self, result)

        # call the result_api
        result_api()

    #******************************
    #* Access Runtime Information
    #*
    #*  runtime information is stored under aetest.runtime. This can be
    #*  accessed during execution (read-only)
    @aetest.subsection
    def access_runtime(self):

        logger.info('Runtime uids: %s' % aetest.runtime.uids)
        logger.info('Runtime groups: %s' % aetest.runtime.groups)

    #******************************
    #* Access Testbed Information
    #*
    #*  when easypy is called with --testbed-file argument, the 'testbed'
    #*  parameter is automatically provided to the testscript with the
    #*  corresponding topology objects.
    #*  in standalone execution, users need to create their own testbed
    #*  argument to pass in the current testbed yaml file, and load it into
    #*  topology objects.
    #*
    #*  this example demonstrate using topology objects, and referencing various
    #*  objects.
    @aetest.subsection
    def print_testbed_information(self, testbed):
        if not testbed or not testbed.devices:
            logger.warning('no testbed was provided to script launch')
        else:
            logger.info('Testbed Name: %s' % testbed.name)
            for device in testbed:
                logger.info('    Device: %s' % device.name)
                for intf in device:
                    logger.info('        Interface: %s' % intf.name)
                    if intf.link:
                        logger.info('            Link: %s' % intf.link.name)
                    else:
                        logger.info('            Link: none')

            # if providing topology information, this is a good place to check
            # that the required information exists.
            if 'routers' in self.parameters:
                # validate each router is in the testbed
                for rtr in self.parameters['routers']:
                    assert rtr in testbed.devices

            if 'links' in self.parameters:
                # validate links
                for link in self.parameters['links']:
                    assert link in testbed.links

        # etc..

    #******************************
    #* Connecting to a device
    #*
    #* Using the Testbed Information, users can connect to their devices
    @aetest.subsection
    def connect_device(self, testbed):
        if not testbed or not testbed.devices:
            logging.warning('No testbed was provided to script launch')
        else:
            # Using the label, connect to the uut device
            if 'labels' in self.parameters:
                if 'uut' in self.parameters['labels'] and\
                   self.parameters['labels']['uut'] in testbed.devices:
                    # store the device into parameters
                    testbed.devices['uut'].connect()
                    self.parent.parameters['uut'] = testbed.devices['uut']

    #******************************
    #* Non Decorated Methods
    #*
    #*  any non @aetest.subsection decorated methods are simply... local class
    #*  methods. They can be used/called in other subsections, but are not
    #*  recognized by the test infrastructure as a valid subsection.
    def random_local_method(self):
        '''Not All Methods Are Subsections

        this can be a great place to put small functions that are shared
        by your multiple subsections

        WARNING:
            - anything that can be used by others should go into a generic lib
            - this is NOT a place to dump your library functions.
        '''

        return "Ooooo, I got called!"


#*******************************************************************************
#* TESTCASE SECTION
#*
class ExampleTestcase(aetest.Testcase):
    '''Defining A Simple Testcase

    Each testcase is broken down into a single optional setup section, multiple
    test sections, and an optional cleanup section.

    Usage:
        - to define a Testcase, create a class that inherits aetest.Testcase
        - use @aetest.setup decorator to mark a method as this testcase's setup
          section. This section is always reported with name "setup". There
          can be only one setup section for a testcase
        - use @aetest.test decorator to mark each individual test method. Each
          method's name will be used as its test uid
        - use @aetest.cleanup decorator to mark a method as this testcase's
          cleanup section. This section is always reported with name "cleanup".
          There can be only one cleanup section for a testcase

    Sequence:
        - setup always runs first
        - tests run after each other in the same sequence as defined in this
          file. in the case of inheritance, the parent class's tests runs first.
        - cleanup always runs last

    Behavior:
        - each testcase must be broken down into smaller tests.
        - all tests are blocked if the setup fails/errors. the cleanup will be
          run in all cases.

    Results:
        - the overall result of Testcase section is calculated as the roll
          up of all its section/tests/cleanup's results. Result roll
          up behavior is well documented with pyats.results module.
        - results for each section/test within a Testcase are collected in the
          same way as subsections in CommonSetup: behavior driven (exceptions)
          or reported using self.<result>() APIs
    '''

    #**********************************
    #* Testcase UID & Description
    #*
    #*   Testcase uid should be unique to a test script. Below is their 
    #*   default values:
    #*
    #*      uid             name of this Testcase class
    #*      description     docstring of this Testcase class
    #*
    #*   To set and alternative uid/description for each testcase, set the
    #*   Testcase class's 'uid' and 'description' attributes. Note that
    #*   uid cannot contain spaces.
    #*
    #*   Example:
    #*
    #*      class MyExampleTestcase(aetest.Testcase):
    #*          '''docstring for this testcase'''
    #*
    #*          uid = 'a_new_uid_for_my_example_testcase'
    #*          description = 'a new description for my example testcase'
    #*
    #*   Note:
    #*      it's best to use to default to using the docstring for testcase
    #*      description

    # set alternative testcase uid & description
    uid = 'ExampleTestcase'
    description = 'An alternative description for this ExampleTestcase'

    #**********************************
    #* Testcase Grouping
    #*
    #*  testcase grouping is an optional feature. It allows users to group/tag
    #*  testcases by common names, and enables group executions where only
    #*  a select groups of testcases is run.
    #*
    #*  associate testcases to groups by by setting its 'groups' attribute with
    #*  a list of groups names (strings). By default, testcases are not
    #*  associated to any groups.
    groups = ['group_A', 'group_B', 'group_C']

    #**********************************
    #* AEtest Feature Parity
    #*
    #*  the following features described in the previous CommonSetup section
    #*  is also 100% applicable to Testcase sections & etc.
    #*
    #*      - result apis
    #*      - behavior driven results:
    #*          - default section result -> Passed
    #*          - AssertionError -> Failed
    #*          - Exceptions -> Errored
    #*      - looping sections (Note, testcases can be looped as well)
    #*      - parameter inheritance from TestScript
    #*      - parameters as function arguments.
    #*      - self is self

    #**********************************
    #* Testcase Parameters
    #*
    #*  testcases may have their own local parameters. These parameters add
    #*  on top of any existing testscript parameters.
    #*
    #*      TestScript -> Testcase -> Setup/Test/Cleanup
    #*
    #*  parameter is a special TestContainer property.
    #*
    #*  The intention of parameters property is to provide a way for users to
    #*  access & store dynamic information, and propagating them between
    #*  testcases and sections. It should not be used to store static values
    #*  as part of a testcase's definition (use testcase data/attribute instead)
    #*
    #*  'parameters' attribute can be set manually as below, providing a method
    #*  to define 'default' parameter values.
    parameters = {
        'local_A': 'default value A',
        'local_B': 'default value B',
    }

    #**********************************
    #* Testcase Data
    #*
    #*  outside of parameters (a parent/child relationship mapping), you can
    #*  also store teatcase data, values/etc as straight up class attributes.
    #*  Keep in mind that Test section parameters cannot be inherited (each
    #*  is its own instances.) Ergo, static variables/data should be defined
    #*  as follows.
    data_A = 1
    data_B = 'xyz'

    #**********************************
    #* Setup Section
    #*
    #*  setup section is optional within each Testcase. It is always run if
    #*  defined. If the setup section's result is not Passed, Passx or Skipped,
    #*  all test sections will be skipped as a consequence.
    #*
    #*  setup section is declared by applying decorator @aetest.setup on a
    #*  Testcase class method.
    #*  setup section is always reported as uid 'setup', regardless of the
    #*  actual method name.
    @aetest.setup
    def setup(self):
        '''Testcase Setup

        This is where configuration specific to this testcase is carried out. In
        addition, this section can also be used to verify that the test targets'
        states are suitable for this testcase to be carried out

        setup section is optional in each testcase.

        Behavior:
            - if this section fails/errors, the rest of this testcase will be
              blocked.
            - if the testcase has cleanup section, cleanup will execute anyways
        '''

        # assign some values to self
        self.awesome = True

        # declare section passed
        self.passed('setup pass')

    #**********************************
    #* Test Section
    #*
    #*  each testcase contains one or more tests. Each test is run one after
    #*  the other, in their defined order.
    #*
    #*  test section is declared by applying decorator @aetest.test on a
    #*  Testcase class method.
    #*  test section uid is reported as the name of the method.
    @aetest.test
    def a_simple_test(self):
        '''A simple Test

        The simplest test section is simply a class method with @aetest.test
        decorator.

        No result APIs are called within this test section, and thus, as it
        exits without error, it will be defaulted to Passed.
        '''

        # let's do some testing
        assert self.awesome is True

        # access attributes/data set within testcase definition
        logger.info('Testcase data_A: %s' % self.data_A)
        logger.info('Testcase data_B: %s' % self.data_B)

    #**********************************
    #* Testscript Parameters
    #*
    #*  setup/test/cleanup sections within testcases also have access to the
    #*  parameters feature, and follows all rules of parameters inheritance.
    #*
    @aetest.test
    def accessing_parameters(self,
                             testbed,
                             parameter_A,
                             parameter_B,
                             local_A,
                             local_B):
        '''Accessing parameters

        In testcases, testcase sections have access to all parent parameters,
        such as TestScript parameters, and Testcase parameters
        '''

        logger.info('Testbed: %s' % testbed)
        logger.info('parameter_A: %s' % parameter_A)
        logger.info('parameter_B: %s' % parameter_B)
        logger.info('local_A: %s' % local_A)
        logger.info('local_B: %s' % local_B)

    @aetest.test
    def accessing_parameters_using_other_methods(self, **kwargs):
        '''Accessing parameters

        Parameters may also accessed by refering to the parameters attribute of
        testcase object, or using **kwargs style input so that all known
        parameters are provided. Both does the same thing.
        '''

        # since they are the same they should be equal
        assert self.parameters == kwargs

        # print parameters into log
        import pprint
        logger.info(pprint.pformat(self.parameters))

    #**********************************
    #* Test Section Looping
    #*
    #*  test sections can be looped by applying the @aetest.loop decorator.
    #*  Each loop iteration receives a unique ID, and is considered a separate
    #*  test altogether (like subsection looping).
    #*
    #*  for this example, we'll use @aetest.test.loop shortcut.
    @aetest.test.loop(index = range(4),
                      result = ['passed', 'failed', 'skipped', 'errored'])
    def looped_test(self, index, result ):
        '''Looped Test

        When loop parameters are defined, it is accessible as a local section
        parameter. Multiple loop parameters can be provided at the same time.
        '''

        logger.info('Current index value: %s' % index)

        # call the result api based on result parameter input
        # equivalent to self.passed(), self.skipped()
        result_api = getattr(self, result)

        # call the result_api
        result_api()

    #**********************************
    #* Result Behaviors Etc
    #*
    #*  the following tests demonstrate result behaviors of Exceptions & etc.
    @aetest.test
    def assert_errors_are_failures(self):
        assert 'Apple' > 'Google', "Apple > Google? Blasphemy! Preposterous!"

    @aetest.test
    def exceptions_are_errors(self, non_existent_parameter):
        '''accessing a non-existent parameter'''
        pass

    @aetest.test
    def show_version(self,uut=None):
        if uut:
            uut.execute('show version')

    #**********************************
    #* Cleanup Section
    #*
    #*  always run last in a testcase, the cleanup section is optional, and,
    #*  when defined, runs regardless of previous testcase/setup pass/fail
    #*  results.
    @aetest.cleanup
    def cleanup(self):
        '''Testcase Cleanup

        Testcase cleanup is always called as a last resort to cleanup the
        test target of any changes made by this testcase. It should be written
        in such a way that it always cleans up what's potentially left behind.

        cleanup section is optional in each testcase.

        '''

        # setting self.parameters = {}
        # note that this only affects local parameters.
        self.parameters = {}


#*******************************************************************************
#* TESTCASE LOOPING
#*
#*  testcases can be looped by applying the @aetest.loop decorator. Any loop
#*  parameter defined in the loop decorator is added to the testcase parameter
#*  dictionary for reference. The following testcase demonstrate this usage.
@aetest.loop(a = [2, 3])
class LoopedTestcase(aetest.Testcase):
    '''Looped Testcase

    In this testcase, we'll demonstrate testcase looping with test looping
    together.
    Testcase looping will apply a testcase parameter named 'a',
    and section looping will apply a section loop parameter 'b'.
    '''

    # associate groups
    groups = ['group_A', 'group_B']

    @aetest.setup
    def setup(self, a):
        logger.info(banner('Value A: %s' % a))

    @aetest.test.loop(b = [4, 5])
    def product(self, a, b):
        logger.info('%s x %s = %s' % (a, b, a*b))


#*******************************************************************************
#* SECTION STEPS
#*
#*  all method sections (subsection, setup, test, cleanup) can be further broken
#*  down into smaller steps, using the step feature. To use, define testsection
#*  methods with 'steps' argument.
#*
#*  if a test section contains steps, at the end of the step, a step report
#*  will be printed.
class TestcaseWithSteps(aetest.Testcase):
    '''Testcase with Steps

    This testcase demonstrate the usage of testcase steps. Note that steps
    applies to subsections in CommonSetup and CommonCleanup as well.
    '''

    # associate groups
    groups = ['group_A', ]

    #**********************************
    #* 'steps'
    #*
    #*  'steps' is a reserved keyword in aetest scripts. using it will allow
    #*  the test infrastructure to bring in steps feature into your local scope
    #*
    #*  Steps Behaviors:
    #*      - defaults to passed
    #*      - if a step Failed, by default, all following steps will not be run.
    #*        this behavior can be averted by providing continue_=True
    #*      - if an assertionError is caught, step -> Failed
    #*      - all other exceptions -> Errored
    @aetest.setup
    def setup(self, steps):
        '''Creating Steps

        Create steps using steps.start() api, which returns a steps context
        manager object. Use it in python's with statement.

        '''
        # to create steps, use 'steps.start()' and 'with' statements.
        with steps.start('this is a description of the step'):
            # steps default to pass - if it ran in full and did not error out
            pass

        with steps.start('another step') as step:
            # step supports the use of result apis:
            step.passed()

    @aetest.test
    def step_continue_on_failure_and_assertions(self, steps):
        '''Steps must pass, unless otherwise indicated

        If step fails, by default, all remaining steps are not run.
        If an assertionError is caught, it is considered Failed() instead of
        Errored().
        '''
        # assertionErrors are also treated as failures
        with steps.start('assertion errors -> Failed', continue_ = True):
            assert 1 == 0

        # this next step can run because previously we set continue_ = True
        # however, keep in mind that even though the step ran, the overall
        # test result is still Failed, due to result rollup rules.
        with steps.start('allowed to continue executing') as step:
            # if we do not set continue_ = True, remaining steps will not run
            self.failed()

        with steps.start('this will not be run'):
            pass

    @aetest.test
    def steps_errors_exits_immediately(self, steps):
        '''Step Errors Exits

        Step errors causes immediate exit of the current section.
        '''
        # assertionErrors are also treated as failures
        with steps.start('exceptions causes all steps to skip over'):
            blablabla_function_doesnt_exist()

        with steps.start('another step that never runs'):
            pass

    @aetest.test
    def steps_with_child_steps(self, steps):
        '''Steps With Child Steps

        Steps can have child steps. This is done by calling step.start() again
        during an existing step. This can be useful when passing the current
        step object into a function, and further dividing that function into
        smaller steps.
        '''

        with steps.start('test step one') as step:
            # start more steps
            with step.start('substep one') as sstep:
                # there's no limit to step nesting
                with sstep.start('subsubstep one') as sstep:
                    with sstep.start('subsubsubstep one') as sstep:
                        with sstep.start('running out of indentation') as sstep:
                            with sstep.start('definitely gone too far...'):
                                pass
            with step.start('substep two') as substep:
                pass
        with steps.start('test step two') as step:
            # call another function, pass in the step
            local_library.function_supporting_step(step)



#*******************************************************************************
#* COMMON CLEANUP SECTION
#*
class CommonCleanup(aetest.CommonCleanup):
    '''Common Cleanup Section

    This is the docstring for your common cleanup section. This section's
    syntax is exactly the same as that of CommonSetup, except its purpose is
    different: CommonCleanup should be the one stop cleaning that removes
    all changes/configurations introduced by this test script on the test
    targets. It is always called.

    Common Cleanup section is optional in a test script.

    Usage:
        - to define a CommonCleanup section, create a class that inherits
          aetest.CommonCleanup class
        - use @aetest.subsection decorator to mark methods in the CommonCleanup
          as a subsection. The name of the function will be used as the
          subsection ID.

    Sequence:
        - CommonCleanup section is always run last in a test script.
        - unless otherwise specified, subsections run after each other in the
          same sequence as defined in this file.
        - in the case of inheritance, the parent class's subsections runs first.

    Behavior:
        - each test script may have only one CommonCleanup section, and must be
          further broken down into subsections
        - all subsections will always run regardless of prior results.

    Results:
        - the overall result of Common Cleanup section is calculated as the roll
          up of all its subsection's results. Result roll up behavior is well
          documented with pyats.results module.
        - results for each subsection within a CommonCleanup section
          are collected in the same way as subsections in CommonSetup: behavior
          driven (exceptions) or reported using self.<result>() APIs
    '''


    #******************************
    #* Example Cleanup Subsection
    #*
    #*  defining the most simplistic subsections.
    #*
    #*  subsection sare defined by applying the @aetest.subsection decorator
    #*  to a method. This marks it as a subsection. The function name is used
    #*  as the subsection id/name.
    @aetest.subsection
    def example_cleanup_subsection(self):
        '''Example Cleanup Subsection'''

        pass

    #******************************
    #* Feature Parity
    #*
    #*  CommonSetup and CommonCleanup features & etc are exactly identical.

    #******************************
    #* Results Default to Passed
    #*
    #*  testscript results defailt to passed, if no exceptions are raised, and
    #*  the section ran to completion.
    @aetest.subsection
    def results_default_to_passed(self):
        '''Results Default to Passed

        The following assertion statement is True, so no error will be raised.
        This section will finish running and automatically receive Passed.

        Manually giving results is so old school ...pffft...
        '''

        # no exception here, and therefore the result for this subsection
        # is a definite Passed
        assert 'Google' > 'Apple', ':) no explanation necessary'


    #******************************
    #* Exception Driven Behavior
    #*
    #*  if an AssertionError is caught, section -> Failed
    @aetest.subsection
    def assertion_error_is_failed(self):
        '''Exception Driven Behavior (Failed)

        In this example, we'll raise an exception to make this section fail.

        '''

        # this will cause an AssertionException
        assert 'I' > "We", 'teamwork is always stronger'

    #******************************
    #* Exception Driven Behavior
    #*
    #*  if any other Exceptions are caught, section -> Failed
    @aetest.subsection
    def exception_driven_behavior_error(self):
        '''Exception Driven Behavior (Errored)

        In this example, we'll cause a python error.

        '''

        # call something that doesn't exist will certainly wreak havoc
        i_am_a_proc_that_does_not_exist('arguments for the win')


#*******************************************************************************
#* STANDALONE EXECUTION
#*
#*   If this script is to be executed in standalone mode, e.g.
#*
#*      bash$ cd /path/to/script
#*      bash$ ./script.py
#*
#*   then the following should be added as the last thing in your test script.
#*******************************************************************************
if __name__ == '__main__':

    #**********************************
    #* Local Imports
    #*
    #*  these imports are here only because they are not required when the
    #*  testscript is normally run, and is only used during standalone runs.
    #*
    #*  this avoids polluting the script namespace

    #
    # local imports
    #
    import argparse
    from pyats import topology

    #**********************************
    #* Log Level
    #*
    #*  set the log level for this run while in standalone mode: you're in
    #*  control of everything.

    #
    # set global loglevel
    #
    logging.root.setLevel('INFO')
    logging.root.setLevel('INFO')

    #**********************************
    #* Standalone Parsers
    #*
    #*  in easypy execution, the infrastructure and the job file passes in
    #*  necessary script arguments. To achieve the same effect in standalone
    #*  execution, you need to create script command-line arguments to do the
    #*  same job.
    #*
    #*  use 'argparse' module.
    #*      https://docs.python.org/3.4/library/argparse.html
    #*
    #*  Guidelines:
    #*      - all custom arguments should start with double dash '--'
    #*      - parsing should only ever be done using parse_known_args(), as
    #*        AEtest also parses its argument during main()
    #*
    #*  in the example below, we've added the --testbed argument for you:
    #*  the equivalent of -testbed_file, loading testbed file into topology
    #*  object.

    #
    # local standalone parsing
    #
    parser = argparse.ArgumentParser(description = "standalone parser")
    parser.add_argument('--testbed', dest = 'testbed',
                        help = 'testbed YAML file',
                        type = topology.loader.load,
                        default = None)

    # do the parsing
    args = parser.parse_known_args()[0]

    #**********************************
    #* aetest.main()
    #*
    #*  this runs the testscript. Pass in any additional script arguments
    #*  in so that it becomes the base part of your testscript parameters.

    #
    # calling aetest.main() to start testscript run
    #
    aetest.main(testbed = args.testbed)
