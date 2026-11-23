"""Show nested loops, custom UIDs and three placements of a retry boundary.

The retry examples deliberately fail west/router1 on its initial attempt.
Each recovers on its first retry and finishes with PASSX. Moving the retry
decorator changes how many loop invocations are repeated.
"""

import logging

from pyats import aetest


logger = logging.getLogger(__name__)


class HierarchicalLoops(aetest.Testcase):
    """Run every device in each region before moving to the next region."""

    @aetest.loop(region=['west', 'east'])
    @aetest.loop(device=['router1', 'router2'])
    @aetest.test
    def check_device(self, region, device):
        """Log one coordinate of the depth-first Cartesian product.

        Args:
            region (str): Current outer-loop value.
            device (str): Current inner-loop value.
        """
        logger.info('region=%s device=%s', region, device)


class CustomLoopUIDs(aetest.Testcase):
    """Replace generated section prefixes with explicit loop UID segments."""

    @aetest.loop(uids=['west'], region=['west'])
    @aetest.loop(uids=['router1', 'router2'], device=['router1', 'router2'])
    @aetest.test
    def check_device(self, region, device):
        """Log explicit UIDs such as west/router1 in the section report.

        Args:
            region (str): Current outer-loop value.
            device (str): Current inner-loop value.
        """
        logger.info('region=%s device=%s', region, device)


class RetryWholeLoop(aetest.Testcase):
    """An outer retry repeats all four region/device combinations."""

    @aetest.retry(retries=1, retry_wait=0)
    @aetest.loop(region=['west', 'east'])
    @aetest.loop(device=['router1', 'router2'])
    @aetest.test
    def check_device(self, region, device, retry_count):
        """Fail once, then replay both loops from their first values.

        Args:
            region (str): Current outer-loop value.
            device (str): Current inner-loop value.
            retry_count (int): Zero for the initial attempt, one for its replay.
        """
        logger.info('region=%s device=%s retry_count=%s', region, device, retry_count)
        if region == 'west' and device == 'router1' and retry_count == 0:
            self.failed('Intentional failure: replay the complete nested loop')


class RetryPerRegion(aetest.Testcase):
    """A retry between loops repeats only the current region's devices."""

    @aetest.loop(region=['west', 'east'])
    @aetest.retry(retries=1, retry_wait=0)
    @aetest.loop(device=['router1', 'router2'])
    @aetest.test
    def check_device(self, region, device, retry_count):
        """Finish and retry west before moving to east.

        Args:
            region (str): Current outer-loop value.
            device (str): Current inner-loop value.
            retry_count (int): Attempt index within the current region.
        """
        logger.info('region=%s device=%s retry_count=%s', region, device, retry_count)
        if region == 'west' and device == 'router1' and retry_count == 0:
            self.failed('Intentional failure: replay only this region')


class RetryPerDevice(aetest.Testcase):
    """A retry inside both loops repeats only the current invocation."""

    @aetest.loop(region=['west', 'east'])
    @aetest.loop(device=['router1', 'router2'])
    @aetest.retry(retries=1, retry_wait=0)
    @aetest.test
    def check_device(self, region, device, retry_count):
        """Retry west/router1 immediately, then continue through the loops.

        Args:
            region (str): Current outer-loop value.
            device (str): Current inner-loop value.
            retry_count (int): Attempt index for this region/device combination.
        """
        logger.info('region=%s device=%s retry_count=%s', region, device, retry_count)
        if region == 'west' and device == 'router1' and retry_count == 0:
            self.failed('Intentional failure: replay only this invocation')


if __name__ == '__main__':
    aetest.main()
