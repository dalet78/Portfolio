import pytest
from locust.env import Environment
from locust.stats import StatsCSVFileWriter
from locust.user.task import TaskSet

from Testing_framework.libs.locust.locust_handler import LocustHandler, set_enviroment
from Testing_framework.framework.resources.helpers.logger import logger


class TestExampleClass:
    @pytest.mark.timeout(600)
    @pytest.mark.sanity
    def test_locust_example(self, test_env):
        """
        Verify locust lobrary
        """
        def _run_main_flow(test):
            logger.info(f"Start test Verify locust library")

            enviroment = set_enviroment()
            http_test = LocustHandler(enviroment=enviroment)
            http_test.run_http_test()

        _run_main_flow(test_env)
    