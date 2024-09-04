import os
import time

from locust import HttpUser, task, between
from Testing_framework.framework.resources.helpers.logger import logger

class LocustHelper(HttpUser):
    wait_time = between(0.1, 5.0)
    url = "/specific-path"  # URL predefinito, può essere modificato con il parametro --url
    host = "http://localhost"  # Host di base predefinito
    total_requests = 0
    successful_requests = 0
    test_duration = 60  # Durata del test in secondi

    def __init__(self, environment):
        super().__init__(environment)
        self.num_requests = environment.user_count
        self.url = environment.parameters.get("url", self.url)
        self.start_time = time.time()

    @task
    def my_task(self):
        logger.info(f"Start ot send multiple http request")
        while time.time() - self.start_time < self.test_duration:
            start_time = time.time()
            response = self.client.get(self.url)
            end_time = time.time()
            self.total_requests += 1
            if response.status_code == 200:
                self.successful_requests += 1
                # logger.info(f"Request succeess {end_time - start_time:.2f}s: {response.text}")
            else:
                logger.error(f"Request fail: {response.text}")
        logger.info(f"Stop ot send multiple http request\n")

    def on_stop(self):
        logger.info(f"Test completed. Total request: {self.total_requests}, Succesful Responce : {self.successful_requests}")
        # return {self.total_requests}, {self.successful_requests}
