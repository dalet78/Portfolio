import time
from typing import Optional
import paramiko
from Testing_framework.framework.resources.helpers.logger import logger

class SshConnectionSingleton:
    """
    A Singleton class for managing SSH connections.
    Ensures only one SSH connection instance exists throughout the application.
    """
    _instance: Optional['SshConnectionSingleton'] = None
    _is_initialized = False

    def __new__(cls):
        """Ensure only one instance of the class is created."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """Initialize the SSH client if not already initialized."""
        if not self._is_initialized:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.hostname = ""
            self.username = ""
            self.password = ""
            self._is_initialized = True

    def initialize(self, hostname: str, username: str, password: str):
        """Set the connection parameters."""
        self.hostname = hostname
        self.username = username
        self.password = password

    def connect(self):
        """Establish the SSH connection."""
        try:
            self.client.connect(hostname=self.hostname, username=self.username, password=self.password)
            logger.info(f'Connection opened with {self.hostname}')
        except Exception as e:
            logger.error(f"Connection failed due to: {e}")
            raise

    def close(self):
        """Close the SSH connection if it's open."""
        if self.client.get_transport():
            self.client.close()
            logger.info(f'Connection closed with {self.hostname}')

    def is_connected(self):
        """Check if the SSH connection is active."""
        return self.client.get_transport() and self.client.get_transport().is_active()

    def reconnect(self, max_attempts: int = 3, delay: int = 5):
        """
        Attempt to reconnect to the SSH server.
        
        Args:
            max_attempts (int): Maximum number of reconnection attempts.
            delay (int): Delay in seconds between reconnection attempts.
        
        Returns:
            bool: True if reconnection was successful, False otherwise.
        """
        for attempt in range(max_attempts):
            try:
                if not self.is_connected():
                    logger.info(f"Attempting to reconnect (attempt {attempt + 1}/{max_attempts})...")
                    self.close()  # Ensure any existing connection is closed
                    self.connect()
                    return True
                else:
                    logger.info("Already connected.")
                    return True
            except Exception as e:
                logger.error(f"Reconnection attempt {attempt + 1} failed: {e}")
                if attempt < max_attempts - 1:
                    time.sleep(delay)
        
        logger.error(f"Failed to reconnect after {max_attempts} attempts.")
        return False