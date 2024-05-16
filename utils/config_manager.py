from model.config import ConfigModel
from view.config import ConfigView
from controller.config import ConfigController

class ConfigManager:
    def __init__(self, config_path="config.yaml"):
        self.config_model = ConfigModel(config_path)
        self.config_view = ConfigView()
        self.config_controller = ConfigController(self.config_model, self.config_view)

    def ensure_config(self):
        config = self.config_controller.ensure_config()
        if config is None:
            raise RuntimeError("Configuration could not be loaded or created.")
        return config
