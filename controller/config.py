class ConfigController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def ensure_config(self):
        config = self.model.load_config()
        if config is None:
            config = self.view.prompt_for_config()
            self.model.save_config(config)
        return config