'''example_job.py

This is the example job file for both comprehensive examples: the base_example
script and variant_example script.

In this jobfile, we'll demonstrate the purpose & configurability of job files,
and as well demonstrate some AEtest features.

Note:
   Any comments with "#*" in front of them (like this entire comment box) are
   for example/infrastructure clarifications only.

Author:
   Siming Yuan, Cisco Systems Inc.

Support:
   pyats-support-ext@cisco.com

Examples:
    # to run under standalone execution
    bash$ python base_example.py

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
# import block
#
import os
import logging
import argparse

from pyats.easypy import run

# import logic statements from datastructures module
from pyats.datastructures.logic import And, Or, Not

#*******************************************************************************
#* ENVIRONMENT
#*
#*   often it may be necessary to parse environment variables to set up script
#*   inputs/arguments based on them. This allows dynamic information from the
#*   environment to control certain behavior of the job.
#*
#*******************************************************************************

#
# logic here to process environment variables.
#
loglevel = os.environ.get('loglevel', 'INFO')
groups = os.environ.get('execution_group', None)
my_variable = os.environ.get('my_variable', 'default_value')

#*******************************************************************************
#* PARSING COMMAND LINE ARGUMENTS
#*
#*  pyATS features argument propagation: propagating custom command
#*  line arguments to jobfile & the testscript. In a nutshell, the requirement
#*  is simple: parse only what you need using parse_known_args(), leave the
#*  rest in sys.argv.
#*
#*  If your jobfile requires additional command line arguments, you'll need to
#*  create an argparse section here.
#*
#*  note - argparse modules are already imported for your convenience above.
#*
#*******************************************************************************

#
# create your custom job file argument parser here
#
parser = argparse.ArgumentParser(description='example job file cli args parser')
parser.add_argument('--argument_a',
                    help='example argument a',
                    default = None)
parser.add_argument('--argument_b',
                    help='example argument b',
                    default = None)


#*******************************************************************************
#* TESTBED INFORMATION
#*
#*  when executing a jobfile using pyats, testbed file should be provided to
#*  pyats launcher using argument --testbed-file. The engine will automatically
#*  load this provided testbed file into topology objects, and pass it to each
#*  testscript as script argument "testbed".
#*       pyats run job myjobfile.py --testbed-file mytestbed.yaml
#*
#*  as long as the argument is used properly, there's nothing extra the user
#*  has to do. Testscripts will automatically be passed the parameter 'testbed',
#*  along with all the topology objects.
#*
#*
#* TOPOLOGY INFORMATION
#*
#*  in an effort to abstract the script's topology/device requirements away
#*  from the actual testbed being used, user may choose to provide certain
#*  alias/uut information as script arguments.
#*
#*  the idea behind it is simple: decouple the testscript from hard-coding
#*  device and interface/link names in the script by:
#*      - providing a label mapping from the jobfile, and/or
#*      - using the topology alias feature.
#*
#*  topology module/objects supports alias-lookups: refering to testbed devices,
#*  links and interfaces by an 'alternative name', which maps to the actual HW
#*  names defined in testbed YAML file. 
#*
#*  in addition, users may also choose to provide a dictionary argument, mapping
#*  labels referenced in the testscript vs actual device names, and make use of
#*  this information within their testscripts. Eg:
#*      labels = {
#*          'pe1': 'device_one',
#*          'uut': 'device_two',
#*      }
#*
#*  it is also a good idea to pass in a list of devices and links to be used
#*  by the testscript. This allows configurability of the testscripts, and
#*  choosing which links/interfaces/devices of the current topology to test on.
#*      routers = ['device_one', 'device_two', 'device_three']
#*      links = ['link_one', 'link_two', 'link_three']
#*      tgns = []
#*
#*  Handling Multiple Testbeds
#*  --------------------------
#*   in the case where your job file is shared across multiple testbeds, you can
#*   test for the current testbed object and set your topology information
#*   accordingly. Eg:
#*
#*      if runtime.testbed:
#*
#*          if runtime.testbed.name == 'testbed_ONE':
#*              labels = {<label mapping for testbed_ONE>}
#*              routers = [<routers to use for testbed_ONE>]
#*              links = [<links to use for testbed_ONE]
#*              tgns = [<tgns to use for testbed_ONE]
#*
#*          elif runtime.testbed.name == 'testbed_TWO'
#*              labels = {<label mapping for testbed_TWO>}
#*              routers = [<routers to use for testbed_TWO>]
#*              links = [<links to use for testbed_TWO]
#*              tgns = [<tgns to use for testbed_TWO
#*
#*      else:
#           # if your script requires a testbed topology, this is a good place
#*          # to throw an exception
#*          raise ValueError('testbed file not provided by -testbed_file')
#*
#*  note - this is simply a typical use-case of aetest testscript arguments. It
#*  is not a hard-coded requirement/input to the infrastructure.
#*******************************************************************************

#
# topology references example definitions
#
labels = {}
routers = []
links = []
tgns = []

# Different routers and labels for another run()
routers2 = ['ott-tb1-n7k3']
labels2 = {
            'uut': 'ott-tb1-n7k3',
          }

#*******************************************************************************
#* MAIN FUNCTION
#*
#*  Each job file must have a main() function where testscripts/task runs are
#*  defined. After a job file is imported, easypy will lookup main() function
#*  to run.
#*
#*  main() funtion shall have a single argument called 'runtime'. This allows
#*  the engine to automatically pass in the current Easypy runtime object. The
#*  following should be performed within the main() function:
#*      - parse any custom command-line arguments
#*      - configure logger log-levels, if any
#*      - run each and every testscript file
#*
#*  Examples
#*  --------
#*
#*      def main(runtime):
#*
#*          # do parse command line job file arguments
#*          args = parser.parse_known_args()
#*
#*          # configure some loggers
#*          logging.getLogger('pyats.aetest').setLevel('DEBUG')
#*          logging.getLogger('mymodule.myfeature').setLevel('INFO')
#*
#*          # simple run
#*          run(testscript = "/path/to/my/script.py", runtime = runtime)
#*
#*          # specify a custom task id
#*          run(testscript = "/path/to/my/script.py",
#*              task_id = "custom_task_id",
#*              runtime = runtime)
#*
#*          # passing script arguments from job file to script
#*          run(testscript = "/path/to/my/script.py",
#*              task_id = "custom_task_id",
#*              runtime = runtime,
#*              script_arg_1 = 'some value 1',
#*              script_arg_2 = 'some value 2',
#*              script_arg_x = 'some value X')
#*
#*          # calling with AEtest options
#*          run(testscript = "/path/to/my/script.py",
#*              submitter = 'chambers',
#*              runtime = runtime)
#*
#*          # making life complicated
#*          run(testscript = "/path/to/my/script.py",
#*              runtime = runtime,
#*              task_id = "custom_task_id",
#*              script_arg_1 = 'some value 1',
#*              script_arg_2 = 'some value 2',
#*              script_arg_x = args.myargument,
#*              submitter = 'chambers')
#*
#*******************************************************************************


#*******************************************************************************
#* SCRIPT ARGUMENTS
#*
#*  Aside from standard run() and aetest infrastructure arguments, all other
#*  keyword arguments (*kwargs) to run() api are effectively script arguments.
#*
#*  Once passed to the testscript, script arguments are updated into testscript
#*  parameters for this run, accessible throughout script sections using the
#*  test-parameters feature. In effect, testcase parameters is a superset of
#*  of the testscript parameters, which itself contains jobfile arguments.
#*
#*          +---------------------------------------------+
#*          | +----------------------------+     testcase |
#*          | | +-----------+   testscript |   parameters |
#*          | | | Job File  |   parameters |              |
#*          | | | arguments |              |              |
#*          | | +-----------+              |              |
#*          | +----------------------------+              |
#*          +---------------------------------------------+
#*
#*  if any jobfile arguments names clash with existing testscript parameters,
#*  it will overwrite the one from the testscript. This allows users to set
#*  default testscript parameters within the script, and use job file arguments
#*  to overwrite them.
#*                          overwrites
#*      Jobfile Arguments --------------> TestScript Parameters.
#*
#*******************************************************************************


# compute the script path from this location
script_path = os.path.join(os.path.dirname(__file__), '..')

#
# main logic, run testscripts inside
#
def main(runtime):

    #
    # parse custom command-line arguments
    #
    custom_args = parser.parse_known_args()[0]

    #**************************************
    #* Log Levels
    #*
    #*  within the job file main() section, you can set the various logger's
    #*  loglevels for your following testscripts. This allows users to modify
    #*  the logging output within the job file, for various modules & etc,
    #*  without modifying testscript and libraries.

    # set log levels for various modules
    # eg, set aetest to INFO, set your library to DEBUG
    logging.getLogger('pyats.aetest').setLevel('INFO')
    logging.getLogger('libs').setLevel('DEBUG')
    logging.getLogger('pyats.aetest').setLevel('INFO')
    logging.getLogger('libs').setLevel('DEBUG')

    #
    # run a test script and provide some script argumentss
    # this will overwrite the default values set in your script.
    # also showing passing topology information arguments into script
    #
    run(testscript= os.path.join(script_path, 'base_example.py'),
        runtime = runtime,
        parameter_A = 'jobfile value A',
        labels = labels,
        routers = routers,
        links = links,
        tgns = tgns)

    #
    # run with a specific router
    #
    run(testscript= os.path.join(script_path, 'base_example.py'),
        runtime = runtime,
        parameter_A = 'jobfile value A',
        labels = labels2,
        routers = routers2,
        links = links,
        tgns = tgns)


    #
    # run the variant script with parsed custom_args and loglevel
    #
    run(testscript= os.path.join(script_path, 'variant_example.py'),
        runtime = runtime,
        loglevel = loglevel,
        **vars(custom_args))

    #**************************************
    #* Run by ID
    #*
    #*  use 'uids' feature to specify which test section uids should run.
    #*  'uids' accepts a callable argument. In this example, instead of writing
    #*  a callable function, we'll leverage datastructure.logic classes.

    #
    # eg, only run testcases with 'Testcase' in the name,
    # but not LoopingTestcase
    #
    run(testscript= os.path.join(script_path, 'base_example.py'),
        runtime = runtime,
        uids = And('.*Testcase.*', Not('ExampleTestcase')))

    #**************************************
    #* Run by Groups
    #*
    #*  use 'groups' feature to specify which testcase groups should run.
    #*  'groups' accepts a callable argument. In this example, we'll also be
    #*  using datastructure.logic classes.

    #
    # eg, only run testcases in group_A and group_C
    #
    run(testscript= os.path.join(script_path, 'variant_example.py'),
        runtime = runtime,
        groups = Or('group_A', 'group_C'))
