import pytest

from Testing_framework.framework.resources.helpers.logger import logger
from Testing_framework.framework.resources.services.ssh_handler import SshHandler


class TestExampleClass:
    @pytest.mark.timeout(600)
    @pytest.mark.sanity
    def test_somma(self, test_env):
        """
        Verify ssh connection library
        """
        def _run_main_flow(test):
            logger.info(f"Start test Verify ssh connection library ")
            """
            MAIN FLOW FUNCTIONS             
            """
            ssh_connection = SshHandler(hostname="192.168.1.138", username="pc-casa\/utente", password="25062013")
            ssh_connection.open_connection()
            ssh_connection.send_command(command= "systeminfo")
            result = ssh_connection.send_command_return_output(command= "systeminfo")
            logger.info(f'result = {result}')
            ssh_connection.close_connection()

        _run_main_flow(test_env)