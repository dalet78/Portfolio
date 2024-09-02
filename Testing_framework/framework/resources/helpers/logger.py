import logging
import time

from art import * 

#from art import *

DEFAULT_LOG_FILENAME = "test.log"  # Improved naming for clarity
NAME = "LOGGER" #Set logger name change with framework name

class LoggerClass:
    """
    Improved Logger class with enhanced features and error handling.

    Example usage:
    logger = LoggerClass()  # Use default log file
    logger.info("This is an informational message.")

    # Optionally change the log file path
    logger.set_log_path("my_custom_log.log")
    logger.warning("This is a warning message.")

    """

    def __init__(self, log_file=DEFAULT_LOG_FILENAME):
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(NAME)
        self.logger.setLevel(logging.DEBUG)
        self.file_log_path = log_file

        try:
            self.set_log_path()
        except (IOError, OSError) as e:  # Handle potential file-related errors
            print(f"Error setting log path: {e}")
            self.logger.error(f"Error setting log path: {e}")  # Log the error

    def set_log_path(self, log_file=None):
        # if log_file:
        #     self.file_log_path = log_file

        # Clear existing handlers (same approach as previous responses)
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

        # Create a new handler with improved formatting and error handling
        try:
            file_handler = logging.FileHandler(self.file_log_path, mode="w")
            file_handler.setLevel(logging.INFO)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler) 

        except (IOError, OSError) as e:
            print(f"Error creating file handler: {e}")
            self.logger.error(f"Error creating file handler: {e}")  # Log the error

    def print_log_title(self) -> None :
        """ Print title of Framework name"""
        self.info(text2art(text=f"\n(((   xxx   )))\n", font="tarty1"))
        self.info("(((xxx))) *** DAVID - AUTOMATION - FRAMEWORK *** (((xxx)))")
        self.debug(f"Log started at {self.file_log_path}")
        time.sleep(0.5)  # delay required to make order of logs prints


    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message): 
        self.logger.critical(message) 


logger = LoggerClass()
