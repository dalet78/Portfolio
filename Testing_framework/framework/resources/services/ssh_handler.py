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
    
    def open_connection(self):
        try:
            self.client.connect(hostname=self.hostname, username=self.username, password=self.password)
            logger.info(f'connection open with {self.hostname}')
        except Exception as e:
            logger.error(f"Open connection fail due: {e}")
            raise e # Re-raise the exception
    
    def close_connection(self):
        if self.client.get_transport():
            self.client.close()
            logger.error(f'Connection close with {self.hostname}')
    
    def send_command(self, command):
        """Sends a command over SSH and logs the output.

        Args:
            command (str): The command to execute on the remote machine.
        """
        self._check_connection_and_handle_errors(command)

    def send_command_return_output(self, command):
        """Sends a command over SSH and returns the output.

        Args:
            command (str): The command to execute on the remote machine.

        Returns:
            str: The standard output of the command, or an empty string if there's an error.
        """
        output = self._check_connection_and_handle_errors(command)
        return output
    
    def _check_connection_and_handle_errors(self, command):
        """
        Checks if the connection is open and handles potential errors during command execution.

        Args:
            command (str): The command to execute on the remote machine.

        Returns:
            str: The standard output of the command.

        Raises:
            Exception: If there is an error executing the command.
        """
        if not self.client.get_transport():
            logger.error(f"Connection to {self.hostname} not opened.")
            return ""

        try:
            stdin, stdout, stderr = self.client.exec_command(command)
            output = stdout.read().decode('utf-8')
            stderr_data = stderr.read().decode('utf-8')

            logger.info(f"Send command output: {output}")
            if stderr_data:
                logger.error(f"Send command output Error: {stderr_data}")
                raise Exception(f"Command execution error: {stderr_data}")
            return output
        except Exception as e:
            logger.error(f"Error sending command: {e}")
            raise e  # Re-raise the exception