import os

from Testing_framework.framework.resources.helpers.logger import logger

PREFIX_SERVER = '[IPERF-SERVER]'
PREFIX_CLIENT = '[IPERF-CLIENT]'

IPERF = 'iperf3'


class _IperfBase:
    """
    Helper class for other classes
    """
    def __init__(self):
        self.logger = logger
        self.server_ip = None
        self.client_ip = None

    def _create_dirs(self):
        self._logger.info(f"{PREFIX_SERVER} Running: {__name__}.create_log_dir")
        

    def _kill_iperf(self):
        self._logger.info(f"Kill {IPERF} on devices")
