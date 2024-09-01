import pytest 

from framework.resources.helpers.logger import logger

SETUP_CONFIG_YAML = "resources.yaml"
PRETEST = "[PRE-TEST]"
POSTEST = "[POST-TEST]"

def _start_test():
    pass

def _finale_test():
    pass

@pytest.fixture(scope = "function")
def _test_env():
    try:
        logger.print_log_title()
        logger.info(f"{PRETEST} STARTED")
        _start_test()
    except Exception as ex:
        raise AssertionError(f"{PRETEST} FAIL: {ex}")
    yield
    try:
        logger.info(f"{POSTEST} *** MAIN POST-TEST STARTED ***")
        _finale_test()
    except Exception as ex:
        raise AssertionError(f"{PRETEST} FAIL: {ex}")

