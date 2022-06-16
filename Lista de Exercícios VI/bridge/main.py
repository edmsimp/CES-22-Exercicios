from vehicle.vehicle import Vehicle
from vehicle.car import Car
from vehicle.bus import Bus
from vehicle.truck import Truck

from engine.eletric_engine import EletricEngine
from engine.combustion_engine import CombustionEngine
from engine.hibrid_engine import HibridEngine

# Client class as it was show in the slides
class Client:
    def __init__(self, vehicle : Vehicle):
        self.vehicle = vehicle

# Usage examples
while(True):
    print("Describe the type of vehicle you want:")
    print("Disponible vehicles: 1 - Car, 2 - Bus, 3 - Truck")
    print("Disponible engines: 1 - Eletric, 2 - Combustion, 3 - Hibrid")
    print("Press Ctrl + C in case you want to exit.")

    v = int(input("Vehicle you want: "))
    e = int(input("Engine you want: "))

    if v == 1:
        if e == 1:
            client = Client(Car(EletricEngine())) # We call the engine part externally from
        elif e == 2:                              # the vehicle type.
            client = Client(Car(CombustionEngine()))
        elif e == 3:
            client = Client(Car(HibridEngine()))
        else:
            print("Invalid input")
    elif v == 2:
        if e == 1:
            client = Client(Bus(EletricEngine()))
        elif e == 2:
            client = Client(Bus(CombustionEngine()))
        elif e == 3:
            client = Client(Bus(HibridEngine()))
        else:
            print("Invalid input")
    elif v == 3:
        if e == 1:
            client = Client(Truck(EletricEngine()))
        elif e == 2:
            client = Client(Truck(CombustionEngine()))
        elif e == 3:
            client = Client(Truck(HibridEngine()))
        else:
            print("Invalid input")
    else: 
        print("Invalid input")