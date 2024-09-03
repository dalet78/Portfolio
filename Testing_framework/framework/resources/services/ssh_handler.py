import paramiko

from Testing_framework.framework.resources.helpers.logger import logger


class SshHandler:
    """
    SSH Handler Class
    """
    def __init__(self, hostname, username, password,  **kwargs):
        self.hostname = hostname
        self.username = username
        self.password = password

        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        self._dict = kwargs.copy()
        self._logger = logger
    
    # @property
    # def name(self) -> str:
    #     """
    #     Get the ip of the external device or service.

    #     @return: The ip of the device or service.
    #     @rtype: str
    #     """
    #     pass
    
    def open_connection(self):
        try:
            self.client.connect(hostname=self.hostname, username=self.username, password=self.password)
            logger.info(f'connection open with {self.hostname}')
        except Exception as e:
            logger.info(f"Open connection fail due: {e}")
    
    def close_connection(self):
        if self.client.get_transport():
            self.client.close()
            logger.info(f'Connection close with {self.hostname}')
    
    def send_command(self, command):
        if self.client.get_transport():
            stdin, stdout, stderr = self.client.exec_command(command)
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')
            logger.info(f"Send command output: {output}")
            if error:
                logger.info(f"Send command output Error: {error}")
        else:
            logger.info(f"Connection to {self.hostname} not opened.")