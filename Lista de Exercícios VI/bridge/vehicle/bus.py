from vehicle.vehicle import Vehicle

class Bus (Vehicle):
    def __init__(self, engine):
        print("bus!\n")
        super().__init__(engine)