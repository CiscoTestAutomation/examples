import logging

from pyats import aetest

logger = logging.getLogger(__name__)

class common_setup(aetest.CommonSetup):

    @aetest.subsection
    def sample_subsection_1(self):
        logger.info("Aetest Common Setup ")

    @aetest.subsection
    def sample_subsection_2(self, section):
        logger.info("Inside %s" % (section))

        logger.info("Inside class %s" % (self.uid))

class tc_one(aetest.Testcase):

    @aetest.setup
    def prepare_testcase(self, section):
        logger.info("Preparing the test")
        logger.info(section)

    @aetest.test
    def simple_test_1(self):
        logger.info("First test section ")

    # Second test section
    @aetest.test
    def simple_test_2(self):
        logger.info("Second test section ")

    @aetest.cleanup
    def clean_testcase(self):
        logger.info("Pass testcase cleanup")


class common_cleanup(aetest.CommonCleanup):
  
    @aetest.subsection
    def clean_everything(self):
        logger.info("Aetest Common Cleanup ")

if __name__ == '__main__': # pragma: no cover
    aetest.main()
