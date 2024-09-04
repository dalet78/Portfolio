import pytest 
import subprocess
import os
import signal
import datetime

from ..framework.resources.helpers.logger import logger
from Testing_framework.libs.dataset.DataSet_Handler import DataSetHandler

SETUP_CONFIG_YAML = "resources.yaml"
PRETEST = "[PRE-TEST]"
POSTEST = "[POST-TEST]"
test_dict = {}


def _start_test():
    test_dict["Test_id"] = "Jira_123"
    test_dict["start_test"] = datetime.datetime.now().strftime("%H:%M:%S")

def _finale_test():
    test_dict["stop_test"] =  datetime.datetime.now().strftime("%H:%M:%S")

@pytest.fixture(scope = "function")
def test_env():
    try:
        logger.print_log_title()
        logger.info(f"{PRETEST} STARTED")
        cmd = "glances --stdout-csv now,cpu.user,mem.used,load > monitoraggio_sistema.csv"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        _start_test()
    except Exception as ex:
        raise AssertionError(f"{PRETEST} FAIL: {ex}")
    yield
    try:
        logger.info(f"{POSTEST} *** MAIN POST-TEST STARTED ***")
        kill_clances_process(process=process)
        _finale_test()
        print_images()
    except Exception as ex:
        raise AssertionError(f"{PRETEST} FAIL: {ex}")

def kill_clances_process(process):
    logger.info(f'kill glances process')
    pid = get_process_pid(process_name="glances")
    logger.info(f'PID: {pid}')
    if pid:
        os.kill(pid, signal.SIGTERM)
    else:
        logger.error("Pid not return correctly")
    
    # process.terminate()
    # try:
    #     process.wait(timeout=5)
    # except subprocess.TimeoutExpired:
    #     process.kill()

    # # Assicurarsi che il processo glances sia terminato
    # for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
    #     if "glances" in proc.info['cmdline']:
    #         proc.terminate()
    #         try:
    #             proc.wait(timeout=5)
    #         except psutil.TimeoutExpired:
    #             proc.kill()

def get_process_pid(process_name):
    logger.info(f'Get PID number of glances')
    output = subprocess.check_output(["ps", "aux"])
    lines = output.decode('utf-8').splitlines()

    for line in lines:
        if process_name in line:
            pid = int(line.split()[1])
            return pid

    return None

def print_images():
    datasethandler = DataSetHandler(csv_file="monitoraggio_sistema.csv", test_dict=test_dict)
    datasethandler.create_df_for_metric()
    datasethandler.plot_cpu_usage()
    datasethandler.plot_ram_usage()
# Esempio di utilizzo:
