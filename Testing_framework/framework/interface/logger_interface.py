from abc import ABC, abstractmethod
from typing import Any
from art import *


class LoggerInterface(ABC):
    @abstractmethod
    def add_handler(self, handler: Any) -> None:
        pass

    @abstractmethod
    def print_log_title(self) -> None:
        pass

    @abstractmethod
    def debug(self, message: str) -> None:
        pass

    @abstractmethod
    def info(self, message: str) -> None:
        pass

    @abstractmethod
    def warning(self, message: str) -> None:
        pass

    @abstractmethod
    def error(self, message: str) -> None:
        pass

    @abstractmethod
    def critical(self, message: str) -> None:
        pass