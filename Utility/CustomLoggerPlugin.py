import logging
import pytest


class CustomLoggerPlugin:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def pytest_runtest_logstart(self, nodeid, location):
        self.logger.info(f"Starting test: {nodeid}")

    def pytest_runtest_report(self, report):
        if report.failed:
            self.logger.error(f"Test failed: {report.nodeid}")
        elif report.skipped:
            self.logger.warning(f"Test skipped: {report.nodeid}")
        else:
            self.logger.info(f"Test passed: {report.nodeid}")

    def pytest_sessionstart(self, session):
        self.logger.info("Test session started")

    def pytest_sessionfinish(self, session, exitstatus):
        self.logger.info("Test session finished")

    def pytest_collection_finish(self, session):
        self.logger.info("Test collection finished")

    def pytest_collection_modifyitems(self, session, config, items):
        for item in items:
            self.logger.debug(f"Test collected: {item.nodeid}")

    def pytest_runtest_setup(self, item, nextitem):
        self.logger.debug(f"Setting up test: {item.nodeid}")

    def pytest_runtest_teardown(self, item, nextitem):
        self.logger.debug(f"Tearing down test: {item.nodeid}")
