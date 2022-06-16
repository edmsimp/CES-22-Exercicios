from vehicle.vehicle import Vehicle

class Car (Vehicle):
    def __init__(self, engine):
        print("car!\n")
        super().__init__(engine)