import pytest 
import subprocess
import os
import signal
import datetime
import pytz
import time

from ..framework.resources.helpers.logger import logger
from Testing_framework.libs.dataset.DataSet_Handler import DataSetHandler
from Testing_framework.framework.resources.helpers.report_builder import ReportBuilder
from Testing_framework.framework.resources.helpers.html_report_builder import HTMLTestReportBuilder
from Testing_framework.framework.core.config.test_config import Config

SETUP_CONFIG_YAML = "resources.yaml"
PRETEST = "[PRE-TEST]"
POSTEST = "[POST-TEST]"
test_dict = {}
tz = pytz.timezone('Asia/Jerusalem')

def _start_test():
    test_dict["Test_id"] = "Jira_123"
    test_dict["Test_description"] = "This dest is sending one http request from multiple users for 60 seconds with intervall variable from 0.1 to 5 sec for user"
    datetime_now_idt = datetime.datetime.now(tz)
    test_dict["start_test"] = datetime_now_idt.strftime("%Y-%m-%d %H:%M:%S %Z")
    logger.info(f"start time = {test_dict['start_test']}")

def _finale_test():
    datetime_now_idt = datetime.datetime.now(tz)
    test_dict["stop_test"] =  datetime_now_idt.strftime("%Y-%m-%d %H:%M:%S %Z")
    logger.info(f"stop time = {test_dict['stop_test']}")

@pytest.fixture(scope = "function")
def test_env():
    try:
        logger.print_log_title()
        logger.info(f"{PRETEST} STARTED")
        cmd = "glances --stdout-csv now,cpu.user,mem.used,load > monitoraggio_sistema.csv"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(2)
        _start_test()
    except Exception as ex:
        raise AssertionError(f"{PRETEST} FAIL: {ex}")
    yield
    try:
        logger.info(f"{POSTEST} *** MAIN POST-TEST STARTED ***")
        _finale_test()
        time.sleep(2)
        kill_clances_process(process=process)
        print_images()
        create_report()

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

def create_report():
    report = HTMLTestReportBuilder("dalet.p@gmail.com", "Ilna2013", "asaf.chepo@gmail.com", "smtp.gmail.com", 587)
    images = [('immagine1.png', 'cpu_usage.png'), ('immagine2.png', 'mem_usage.png')]
    log_file = 'test.log'
    report.build_and_send_report(test_dict, images, log_file )

def send_report():
    pass

@pytest.fixture(scope='session')
def config(request):
    config_obj = Config()
    setup_name = request.config.getoption("--setup")
    return config_obj.get_setup_data(setup_name)