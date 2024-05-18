import yaml
import os

class ConfigModel:
    def __init__(self, config_path="config.yaml"):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_path):
            return None
        with open(self.config_path, "r") as f:
            config = yaml.safe_load(f)
        return config
    
    
    def load_bulk_file_config(self, key_file_path):
        if "bulkfile" in self.config and key_file_path in self.config["bulkfile"]:
            return self.config["bulkfile"][key_file_path]
        else:
            return None

    def save_config(self, config):
        with open(self.config_path, "w") as f:
            yaml.safe_dump(config, f)
        self.config = config

    def __getitem__(self, item):
        return self.config[item]
