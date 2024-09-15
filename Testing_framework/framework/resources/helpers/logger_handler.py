from abc import ABC, abstractmethod
from typing import Any
import logging
import time
from art import *
from Testing_framework.framework.interface.logger_interface import LoggerInterface 

DEFAULT_LOG_FILENAME = "test.log"  # Improved naming for clarity
NAME = "LOGGER" #Set logger name change with framework name

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
             self.file_handler.emit(logging.makeLogRecord({
            "name": "",
            "level": level,
            "pathname": "",
            "lineno": 0,
            "msg": message,
            "args": None,
            "exc_info": None
        }))


class PrintLogHandler(LogHandler):
    """
    Concrete implementation of a log handler printing to the console.
    """

    def handle(self, message, level):
        print(message)


class LoggerClass(LoggerInterface):
    def __init__(self):
        self.handlers = []
        logging.basicConfig(level=logging.DEBUG)
        self.logger = logging.getLogger(NAME)
        self.logger.setLevel(logging.DEBUG)

    def add_handler(self, handler: Any) -> None:
        self.handlers.append(handler)
        self.logger.addHandler(handler.file_handler if isinstance(handler, FileLogHandler) else handler)

    def print_log_title(self) -> None:
        self.info(text2art(text=f"\n(((   xxx   )))\n", font="tarty1"))
        self.info("(((xxx))) *** DAVID - AUTOMATION - FRAMEWORK *** (((xxx)))")
        self.debug(f"Log started at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(0.5)

    def debug(self, message: str) -> None:
        self._log(message, logging.DEBUG)

    def info(self, message: str) -> None:
        self._log(message, logging.INFO)

    def warning(self, message: str) -> None:
        self._log(message, logging.WARNING)

    def error(self, message: str) -> None:
        self._log(message, logging.ERROR)

    def critical(self, message: str) -> None:
        self._log(message, logging.CRITICAL)

    def _log(self, message: str, level: int) -> None:
        for handler in self.handlers:
            handler.handle(message, level)

# Usa il logger
logger: LoggerInterface = LoggerClass()
logger.add_handler(FileLogHandler(DEFAULT_LOG_FILENAME))
logger.add_handler(PrintLogHandler())