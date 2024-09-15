import pytest

from Testing_framework.framework.resources.helpers.logger_handler import logger
from Testing_framework.framework.resources.services.ssh_commander import EnhancedSshCommander


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
            ssh_connection = EnhancedSshCommander(hostname="192.168.1.138", username="pc-casa\/utente", password="25062013")
            result = ssh_connection.send_command(command= "systeminfo")
            logger.info(f'result = {result}')
            

        _run_main_flow(test_env)

    # @pytest.mark.timeout(600)
    # @pytest.mark.sanity
    # def test_downlink_iperf(self, test_env):
    #     """
    #     Verify ssh connection library
    #     """
    #     def _run_main_flow(test):
    #         logger.info(f"Start test Verify ssh connection library ")
    #         """
    #         MAIN FLOW FUNCTIONS             
    #         """
    #         run_iperf_on_server()
    #         run_iperf_on_client()
    #         verify_result()

    #     _run_main_flow(test_env)