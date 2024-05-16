class Identity:
    def __init__(self, identity_id):
        self.identity_id = identity_id
        self.attributes = self.load_attributes()

    def load_attributes(self) -> {}:
        pass

    def __getitem__(self, item):
        return self.attributes.get(item)
