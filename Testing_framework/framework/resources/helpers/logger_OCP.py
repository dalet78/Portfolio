import logging
import time
from abc import ABC, abstractmethod

from art import *


class LogHandler(ABC):
    """
    Abstract class representing a log handler.
    """

    @abstractmethod
    def handle(self, message, level):
        pass


class FileLogHandler(LogHandler):
    """
    Concrete implementation of a log handler writing to a file.
    """

    def __init__(self, log_file):
        self.file_handler = logging.FileHandler(log_file, mode="w")
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.file_handler.setFormatter(self.formatter)

    def handle(self, message, level):
        if level >= logging.INFO:
            self.file_handler.emit(logging.makeRecord(
                "", level, "", "", message, "", "", 0))


class PrintLogHandler(LogHandler):
    """
    Concrete implementation of a log handler printing to the console.
    """

    def handle(self, message, level):
        print(message)


class LoggerClass:
    """
    Improved Logger class with enhanced features and error handling.

    Example usage:
    logger = LoggerClass()  # Use default log handlers

    # Add custom log handlers
    logger.add_handler(FileLogHandler("my_custom_log.log"))
    logger.add_handler(PrintLogHandler())

    logger.info("This is an informational message.")
    """

    def __init__(self):
        self.handlers = []
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger("LOGGER")
        self.logger.setLevel(logging.DEBUG)

    def add_handler(self, handler: LogHandler):
        """
        Add a custom log handler to the logger.
        """
        self.handlers.append(handler)
        self.logger.addHandler(handler.file_handler if isinstance(handler, FileLogHandler) else handler)

    def print_log_title(self) -> None:
        """ Print title of Framework name"""
        self.info(text2art(text=f"\n(((   xxx   )))\n", font="tarty1"))
        self.info("(((xxx))) *** DAVID - AUTOMATION - FRAMEWORK *** (((xxx)))")
        self.debug(f"Log started at {time.strftime('%Y-%m-%d %H:%M:%S')}")  # Use strftime for better formatting
        time.sleep(0.5)  # delay required to make order of logs prints

    def debug(self, message):
        """
        Log message at debug level.
        """
        self._log(message, logging.DEBUG)

    def info(self, message):
        """
        Log message at info level.
        """
        self._log(message, logging.INFO)

    # ... other logging methods (warning, error, critical) with similar implementation

    def _log(self, message, level):
        for handler in self.handlers:
            handler.handle(message, level)


logger = LoggerClass()