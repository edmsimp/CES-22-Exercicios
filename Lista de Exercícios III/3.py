"""
3) Crie um exemplo com herança múltipla. Teste o comportamento do método
super() com heranças múltiplas criando um método que faz uso das
implementações nas superclasses.

"""

class Car():
    """
    Represents a car.
    
    """

    def set_velocity(self, velocity):
        """
        Sets the car velocity.

        :param velocity: car velocity.
        :type velocity: int.
        """

        self.v = velocity

class Boat():
    """
    Represents a boat.
    
    """

    def set_w_velocity(self, water_velocity):
        """
        Sets the boat velocity on water.

        :param water_velocity: boat velocity on water.
        :type water_velocity: int.
        """

        self.w_v = water_velocity

class AmphibiousCar(Car, Boat):
    """
    Represents an amphibious car.
    
    """

    def set_velocities(self, velocity, water_velocity):
        """
        Sets the car velocity on and off water and print it.

        :param velocity: off water velocity.
        :type velocity: int.
        :param water_velocity: on water velocity.
        :type water_velocity: int.
        """

        super().set_velocity(velocity)
        super().set_w_velocity(water_velocity)

        print("Off water velocity: ", self.v, "m/s\nOn water velocity: ", self.w_v, "m/s\n")    

##### Usage examples #####

teste = AmphibiousCar()
teste.set_velocities(2, 1) # Super methods being called
