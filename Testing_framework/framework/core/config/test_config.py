import yaml
import pytest

CONFIG_YAML = "resources.yaml"

class Config:
    def __init__(self, config_file='resources.yaml'):
        with open(config_file) as f:
            self.config = yaml.safe_load(f)

    def get_setup_data(self, setup_name):
        if setup_name not in self.config['test_data']:
            raise ValueError(f"Invalid setup name: {setup_name}")
        return self.config['test_data'][setup_name]
