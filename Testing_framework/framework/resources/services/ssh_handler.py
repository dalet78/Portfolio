from fabric import Connection, Config, Result
from invoke import Failure
from paramiko.sftp_client import SFTPClient
from paramiko.ssh_exception import SSHException
from timeout_function_decorator import timeout as ssh_timeout

from Testing_framework.framework.resources.helpers.logger import logger


class SshHandler:
    """
    SSH Handler Class
    """
    def __init__(self, **kwargs):
        self._dict = kwargs.copy()
        self._logger = logger
    
    @property
    def name(self) -> str:
        """
        Get the ip of the external device or service.

        @return: The ip of the device or service.
        @rtype: str
        """
        return str(self._dict.get('name', 'ssh'))
    
    @ssh_timeout(15)
    def connect(self)-> None | Exception:
        """
        Establishes a connection with the external device or service.

        @return: None if the connection was successfully established,
            otherwise an Exception may be raised to indicate the nature of the failure.
        @rtype: None | Exception

        @raise Exception: Specific exceptions may be raised by subclasses to indicate various failure conditions
            during the connection process.
        """
        self._logger.debug(f"Initiate SSH connection to {self.name.upper()}..")
        self.close()
        self.connection.open()
        self._connection_failure = 0

    def close(self):
        pass

    def reconnect(self) -> bool:
        pass

    def send(self, command: str, *args, **kwargs):
        """
        Method that override 'send' function from interact layer. Especially add prefix to executed command
        @param command: sh command to execute
        @param args:
        @param kwargs:
        @return:
        """
        pass

    def connection(self) -> Connection:
        """
        Provides access to the current connection object used for communication with the external device.

        @return: The current SSH connection object associated with the external device or service.
        @rtype: Connection
        """
        if self._connection is not None and self._connection.is_connected:
            self._logger.debug(f"[{self.name}] Connection is: {self._connection.is_connected}")

            return self._connection

        if self._connection is not None:
            self._connection.close()

        connect_kwargs = {
            'password': self._dict.get('host_password'),
            'allow_agent': False,
            'look_for_keys': False,
            'timeout': 60,
            'auth_timeout': 5
        }

        config = Config(overrides={'sudo': {'password': self._dict.get('host_password')}})

        self._connection = Connection(
            host=self._dict.get('host_ip'),
            user=self._dict.get('host_user'),
            gateway=self.gateway,
            config=config,
            connect_kwargs=connect_kwargs
        )

        return self._connection