from engine.engine import Engine

class Vehicle:
    def __init__(self, engine):
        self.engine = engine # Call the engine type from an external class
        # TODO: add some extra logic if needed, this is
        # supposed to be only an abstract class