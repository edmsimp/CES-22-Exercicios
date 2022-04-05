"""
3) Crie um exemplo com herança múltipla. Teste o comportamento do método
super() com heranças múltiplas criando um método que faz uso das
implementações nas superclasses.

"""

class ModeOfTransport():
    """
    Represents a mode of transport.
    
    """
    
    def set_velocity(self, velocity):
        """
        Sets the velocity.

        :param velocity: velocity.
        :type velocity: int.
        """

        self.v = velocity

class Car(ModeOfTransport):
    """
    Represents a car.
    
    """

    def set_velocity(self, velocity):
        """
        Sets the car velocity.

        :param velocity: car velocity.
        :type velocity: int.
        """
        super().set_velocity(velocity)

class Boat(ModeOfTransport):
    """
    Represents a boat.
    
    """

    def set_velocity(self, water_velocity):
        """
        Sets the boat velocity on water.

        :param water_velocity: boat velocity on water.
        :type water_velocity: int.
        """
        velocity = water_velocity
        super().set_velocity(velocity)

class AmphibiousCar(Car, Boat):
    """
    Represents an amphibious car.
    
    """

    def set_velocities(self, velocity, water_velocity, state):
        """
        Sets the car velocity on and off water and print it.

        :param velocity: off water velocity.
        :type velocity: int.
        :param water_velocity: on water velocity.
        :type water_velocity: int.
        """
        if state == 'ground':
            super().set_velocity(velocity)
        elif state == 'water':
            super().set_velocity(water_velocity)

        print("state: " + state + ", " + str(self.v) + " m/s")    

##### Usage examples #####

teste = AmphibiousCar()
teste.set_velocities(2, 1, 'water') # Super methods being called
