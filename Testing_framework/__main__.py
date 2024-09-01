from framework.resources.helpers.logger import logger
from framework.resources.helpers.version import print_framework_version

def create_logger_file() ->None:
    logger.set_log_path()

def main() -> None :
    create_logger_file()
    print_framework_version()
    

if __name__ == "__main__":
    main()