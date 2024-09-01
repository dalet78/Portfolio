from framework.resources.helpers.logger import LoggerClass
from framework.resources.helpers.version import print_framework_version

def set_logger_file(file_log_path = None) ->None:
    logger = LoggerClass()
    if file_log_path: 
        logger.set_log_path(file_log_path)
    else:
        logger.set_log_path()

def main() -> None :
    set_logger_file()
    print_framework_version()
    

if __name__ == "__main__":
    main()