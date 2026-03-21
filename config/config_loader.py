import yaml
import os

def load_config():
    env = os.getenv("TEST_ENV", "staging")

    with open("config/config.yaml", "r") as file:
        data = yaml.safe_load(file)

    return data[env]