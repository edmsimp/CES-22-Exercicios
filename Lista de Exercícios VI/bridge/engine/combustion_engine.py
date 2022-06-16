from engine.engine import Engine

class CombustionEngine (Engine):
    def __init__(self):
        super().__init__()
        print("Combustion engine", end=' ')