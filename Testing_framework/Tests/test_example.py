import pytest
from Testing_framework.framework.resources.helpers.logger import logger

def somma(a, b):
    return a + b

class TestExampleClass:
    @pytest.mark.timeout(600)
    @pytest.mark.sanity
    def test_somma(self, test_env):
        """
        Verify somma function
        """
        def _run_main_flow(test):
            logger.info(f"Start test Verify Somma ")
            """
            MAIN FLOW FUNCTIONS             
            """
            assert somma(2, 3) == 5

        _run_main_flow(test_env)
    