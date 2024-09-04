import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import datetime

class DataSetHandler():
    def __init__(self, csv_file=None, test_dict=None) -> None:
        if test_dict is None:
            raise ValueError("test_dict argument is required")
        self.df = pd.read_csv(csv_file)
        self.test_id = test_dict["Test_id"]
        self.start_test = test_dict["start_test"]
        self.stop_test = test_dict["stop_test"]

    def create_df_for_metric(self):
        self.cpu_df = self.df[["now.custom", "cpu.user"]]
        self.mem_df = self.df[["now.custom", "mem.used"]]
    
    def plot_cpu_usage(self):
        plt.figure(figsize=(10, 6))

        # Creiamo una lista con i timestamp di inizio e fine
        x_ticks = [self.start_test, self.stop_test]

        # Plottiamo i dati, usando x_ticks come asse x
        plt.plot(x_ticks, self.cpu_df["cpu.user"], color="blue")
        plt.xlabel("Time")
        plt.ylabel("CPU Usage (%)")
        plt.title(f"CPU Usage - Test ID: {self.test_id}")
        plt.xticks(x_ticks, labels=["Start", "Stop"])

        plt.grid(True)
        plt.legend()  # Show labels for vertical lines
        plt.savefig("cpu_usage.png")

    
    def plot_ram_usage(self):
        plt.figure(figsize=(10, 6))

        # Creiamo una lista con i timestamp di inizio e fine
        x_ticks = [self.start_test, self.stop_test]

        # Plottiamo i dati, usando x_ticks come asse x
        plt.plot(x_ticks, self.mem_df["mem.used"], color="green")
        plt.xlabel("Time")
        plt.ylabel("Memory Usage (bytes)")
        plt.title(f"Memory Usage - Test ID: {self.test_id}")

        # Impostiamo i tick sull'asse x per visualizzare solo i timestamp di inizio e fine
        plt.xticks(x_ticks, labels=["Start", "Stop"])
        
        # Impostiamo i tick sull'asse x per visualizzare solo i timestamp di inizio e fine
        plt.xticks(x_ticks, labels=["Start", "Stop"])

        plt.grid(True)
        plt.legend()  # Show labels for vertical lines
        plt.savefig("mem_usage.png")


