import os
import time

from Testing_framework.framework.resources.helpers.logger import logger
from iperf_helper import IPERF, _IperfBase


class Iperf(_IperfBase):
    """
    Main class with functionality for Influx DB manipulations
    """

    def __init__(self, port = None):
        super().__init__()
        self._create_dirs()
        self._kill_iperf()
        self.port = None
        self.logger = logger

    def start_iperf_server(self, ip=None):
        """
        Iperf3 Start Server on pc function
        kill old iPerf process if running
        delete old json file is exists
        start server on Ipc
        """
        self.logger.info(f"Running: {__name__}.start_server")
        self._start_server()
    
    def start_iperf_client(self, ip_client=None, is_udp = False, interval=1, duration=120, bandwidth=250, length=8000, num_session= 1):
        """
        Iperf3 Start Client function
        kill old iPerf process if running
        delete old json file is exists
        start udp client on acp
        @param interval: 1
        @param duration: 120 seconds
        @param bandwidth: 250
        @param length:
        """
        self.logger.info(f"Running: {__name__}.start_udp_client")
        self._start_client(ip = ip_client,  is_udp=is_udp, interval=interval, duration=duration,
                           bandwidth=bandwidth, length=length)
        
    def _start_server(self):
        cmd = [IPERF, '-s']
        if self.port:
            cmd += ['-p', str(self.port)]

        filename = f"iperf_server_{self._test.acp.soc(0).name}"
        self.server_json_name = "server_result.json"

        cmd += ['-J', '--logfile', self.server_json_name]

        return self._test.acp.soc(0).os.start_process_in_background(' '.join(cmd))
    
    def _start_client(self, ip_client, is_udp, bandwidth=250, length=None, interval=1, duration=120, sessions=4,
                      parallel=""):
        
        filename = f"iperf_client_{self._test.ctrl.name}"
        ctrl_path = self._test.ctrl.get_temp_log_dir()

        self.client_json_name = self._test.ctrl.os.normalize_path(
            Path(ctrl_path) / 'soc0' / self._test.ctrl.os.generate_temp_filename(filename, '.json'))

        stop_flag = False

        def _print_remaining_time(dur_sec):
            target_time = time.time() + dur_sec
            self._logger.info(f"iPerf transmission will run for {dur_sec} seconds")
            while not stop_flag:
                remaining_time = target_time - time.time()
                if remaining_time < 0:
                    break
                sleep_duration = random.randint(1, 5)
                self._logger.debug(f"iPerf session remaining time: {remaining_time:.0f} sec")
                time.sleep(sleep_duration)
            self._logger.info(f"iPerf transmission completed")

        port = f"-p {self.port}" if self.port else ""
        if_length = f"--length {length}" if length else ""
        if_parallel = f"--parallel {parallel}" if parallel else ""
        udp = f"--udp -b {bandwidth}M {if_length} " if is_udp else ""
        server_ip = self._remote_host.get_acp_ip()
        if on_acp:
            server_ip = self._test.get_setup_details.ctrl.soc0_ip
        if interval > 60:
            self._logger.raise_assertion(f"interval: {interval} > 60 set it to value less then 60 !!!")
        cmd = f"iperf3 -c {server_ip} {port} {udp}-J --logfile {self.client_json_name} {if_parallel}" \
              f"-i {interval} -t {duration} -P {sessions}"

        # Create and start the time thread
        time_thread = threading.Thread(target=lambda: _print_remaining_time(duration))
        time_thread.start()

        try:
            # Create and start the time thread
            self._remote_host.send_command(cmd, on_acp=on_acp, on_ipc=on_ipc, ssh_should_fail=True,
                                           timeout=int(duration) + 10)
        finally:
            # Stop time thread
            stop_flag = True
            time_thread.join()
            self._remote_host.send_command(f"cat {self.client_json_name}", on_acp=on_acp, on_ipc=on_ipc)
