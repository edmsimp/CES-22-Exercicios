from vehicle.vehicle import Vehicle

class Truck (Vehicle):
    def __init__(self, engine):
        print("truck!\n")
        super().__init__(engine)