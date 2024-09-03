from .logger import logger


def get_framework_version():
    return "version 0.0.1"

def print_framework_version() ->None:
    framework_version = get_framework_version()
    logger.info(message=f'Testing framework: {framework_version}')

