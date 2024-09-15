from abc import ABC, abstractmethod
from typing import Optional
from Testing_framework.framework.resources.helpers.logger import logger
from .ssh_connection_handler import SshConnectionSingleton

class SshInterface(ABC):
    """
    Abstract base class defining the interface for SSH operations.
    """
    @abstractmethod
    def send_command(self, command: str) -> str:
        """
        Send a command over SSH and return the output.

        Args:
            command (str): The command to execute.

        Returns:
            str: The output of the executed command.
        """
        pass

    @abstractmethod
    def send_command_in_background(self, command: str) -> None:
        """
        Send a command to be executed in the background on the SSH server.

        Args:
            command (str): The command to execute in the background.
        """
        pass

class EnhancedSshCommander(SshInterface):
    """
    Implementation of the SshInterface using SshConnectionSingleton.
    Provides enhanced functionality including automatic reconnection.
    """
    def __init__(self, hostname: str, username: str, password: str):
        """
        Initialize the EnhancedSshCommander with connection details.

        Args:
            hostname (str): The hostname or IP address of the SSH server.
            username (str): The username for SSH authentication.
            password (str): The password for SSH authentication.
        """
        self.connection = SshConnectionSingleton()
        self.connection.initialize(hostname, username, password)

    def __enter__(self):
        """Context manager entry point: establish the SSH connection."""
        self.connection.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point: close the SSH connection."""
        self.connection.close()

    def send_command(self, command: str) -> str:
        """
        Send a command over SSH and return the output.
        Automatically handles reconnection if the connection is lost.

        Args:
            command (str): The command to execute over SSH.

        Returns:
            str: The output of the executed command.

        Raises:
            Exception: If unable to execute the command after reconnection attempts.
        """
        if not self.connection.is_connected():
            self.connection.reconnect()
        
        try:
            stdin, stdout, stderr = self.connection.client.exec_command(command)
            output = stdout.read().decode('utf-8', errors='ignore')
            error = stderr.read().decode('utf-8', errors='ignore')
            if error:
                logger.error(f"Command error: {error}")
            return output
        except Exception as e:
            logger.error(f"Error sending command: {e}")
            if not self.connection.reconnect():
                raise Exception("Failed to reconnect and execute command")
            return self.send_command(command)  # Retry after reconnection

    def send_command_in_background(self, command: str) -> None:
        """
        Send a command to be executed in the background on the SSH server.

        Args:
            command (str): The command to execute in the background.
        """
        background_command = f"nohup {command} > /dev/null 2>&1 &"
        output = self.send_command(background_command)
        logger.info(f"Command '{command}' sent to run in background. Output: {output}")