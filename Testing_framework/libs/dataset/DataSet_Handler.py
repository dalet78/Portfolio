import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import datetime

from Testing_framework.framework.resources.helpers.logger import logger

class DataSetHandler():
    def __init__(self, csv_file=None, test_dict=None) -> None:
        if test_dict is None:
            raise ValueError("test_dict argument is required")
        self.df = pd.read_csv(csv_file)
        self.test_id = test_dict["Test_id"]
        self.start_test = test_dict["start_test"]
        logger.info(f"stop time = {self.start_test}")
        self.stop_test = test_dict["stop_test"]
        logger.info(f"stop time = {self.stop_test}")

    def create_df_for_metric(self):
        self.x_time = self.df["now.custom"]
        self.cpu_df = self.df["cpu.user"]
        self.mem_df = self.df["mem.used"]
    
    def plot_cpu_usage(self):
        # Plottiamo i dati, usando x_ticks come asse x
        plt.plot(self.x_time , self.cpu_df, color="blue")
        plt.xticks([])
        plt.axvline(x=self.start_test, color='green', linestyle='--')
        plt.axvline(x=self.stop_test, color='red', linestyle='--')

        plt.xlabel("Time")
        plt.ylabel("CPU Usage (%)")
        plt.title(f"CPU Usage - Test ID: {self.test_id}")
        # plt.xticks(x_ticks, labels=["Start", "Stop"])

        plt.grid(True)
        plt.legend()  # Show labels for vertical lines
        plt.savefig("cpu_usage.png")

    
    def plot_ram_usage(self):
        plt.figure(figsize=(10, 6))

        # Plottiamo i dati, usando x_ticks come asse x
        plt.plot(self.x_time, self.mem_df, color="blue")
        plt.xticks([])
        plt.axvline(x=self.start_test, color='green', linestyle='--')
        plt.axvline(x=self.stop_test, color='red', linestyle='--')
        plt.xlabel("Time")
        plt.ylabel("Memory Usage (bytes)")
        plt.title(f"Memory Usage - Test ID: {self.test_id}")

        plt.grid(True)
        plt.legend()  
        plt.savefig("mem_usage.png")


