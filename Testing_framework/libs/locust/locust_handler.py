from locust.env import Environment
from locust.stats import StatsCSVFileWriter
from locust.user.task import TaskSet

from Testing_framework.libs.locust.locust_helper import LocustHelper
from Testing_framework.framework.resources.helpers.logger import logger


def set_enviroment():
        logger.info(f"Set enviroment configuration")
        environment = Environment(user_classes=[LocustHelper])

        # Crea l'ambiente simulato per Locust
        environment.user_count = 10  # Puoi personalizzare user_count secondo le tue esigenze
        environment.parameters = {"url": "http://localhost/specific-path"}
        return environment

class LocustHandler(LocustHelper):
    def __init__(self, enviroment):
        self.environment = enviroment
    
    def run_http_test(self):
        # Crea un'istanza di LocustHandler con l'ambiente creato
        logger.info(f"Start http test on server")
        http_test = LocustHelper(environment=self.environment)

        # Esegui il test task
        http_test.my_task()
        http_test.on_stop()

    

        # # Configura StatsCSVFileWriter per scrivere le statistiche in un file CSV
        # stats_file_path = "test_results"  # Specifica il percorso del file CSV
        # percentiles_to_report = [50.0, 90.0, 95.0, 99.0]  # Percentili da includere nel report
        # stats_csv_writer = StatsCSVFileWriter(environment,percentiles_to_report=percentiles_to_report, base_filepath=stats_file_path)
        # stats_csv_writer.

