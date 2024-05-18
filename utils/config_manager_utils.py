from model.config_model import ConfigModel
from view.config_view import ConfigView
from controller.config_controller import ConfigController
from utils.logger_utils import log

class ConfigManager:
    def __init__(self, config_path="config.yaml"):
        self.config_model = ConfigModel(config_path)
        self.config_view = ConfigView()
        self.config_controller = ConfigController(self.config_model, self.config_view)

    def ensure_config(self):
        config = self.config_controller.ensure_config()
        if config is None:
            log.error("Configuration could not be loaded or created.")
            raise RuntimeError("Configuration could not be loaded or created.")
        return config
    
    def ensure_bulk_operation_file(self,key_file_path):
        config = self.config_controller.ensure_bulk_operation_configuration(key_file_path)
        if config is None:
            log.error("Bulk operation source could not be loaded or created")
            raise RuntimeError("Bulk operation source could not be loaded or created")
        return config
    
