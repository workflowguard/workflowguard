__version__ = "0.0.1"


class State:
    """A State class"""
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
