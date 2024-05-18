from model.config_model import ConfigModel
from view.config_view import ConfigView


class ConfigController:
    def __init__(self, model: ConfigModel, view: ConfigView):
        self.model = model
        self.view = view
        self.config_content = {}

    def ensure_config(self):
        config = self.model.load_config()
        if config is None:
            config = self.view.prompt_for_config()
            self.model.save_config(config)
            self.config_content = config
        return self.config_content

    def ensure_bulk_operation_configuration(self,key_file_path):
        bulk_file_config = self.model.load_bulk_file_config(key_file_path)
        if bulk_file_config is None:
            bulk_file_config = self.view.prompt_bulk_file_config(key_file_path)
            if 'bulkfile' not in self.config_content:
                self.config_content['bulkfile'] = {}
            self.config_content['bulkfile'] = bulk_file_config
            
            self.model.save_config(self.config_content)

        return self.config_content