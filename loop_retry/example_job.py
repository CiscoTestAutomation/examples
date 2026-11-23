"""Run the hierarchical loop and retry examples without a device testbed."""

from pathlib import Path

from pyats.easypy import run


def main():
    """Run the test script located next to this job file."""
    run(testscript=str(Path(__file__).with_name('example_script.py')))
