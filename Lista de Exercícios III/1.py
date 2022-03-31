"""
1) Crie exemplos que ilustrem as diferenças e as vantagens entre métodos
abstratos, métodos estáticos, métodos de classe e métodos de instância.

"""

from abc import abstractmethod

class City:
    """
    Represents a city.
    
    """
    def __init__(self, name, habitants):
        """
        Creates a city.

        :param name: habitants of the city.
        :type name: string.
        :param habitants: number of habitants of the city.
        :type habitants: int.
        """

        self.name = name
        self.habitants = habitants

    # Example of abstract method. It's not defined in the City class, but
    # only in child classes, then it is only usable in these.
    @abstractmethod
    def age(self):
        pass

    # Two examples of instance method. It's only callable by an instance
    # of the city class and have access to the class' parameters, being
    # able to change and return it.
    def change_name(self, name):
        """
        Changes the name of the city.
        
        :param name: habitants of the city.
        :type name: string.
        """

        self.name = name

    def print_name(self):
        """
        Prints the name of the city.

        """
        
        print(self.name,'\n')

    
    # Example of class method. Does not need a instance of the city
    # class to be called and have access to the class' parameters, being
    # able to change and return it. Usually used as a new constructor.
    @classmethod
    def from_name(cls, name):
        """
        Creates a city from it's name. Only a few names are stored in the database.

        :param name: name of the city.
        :type name: string.
        :rtype: City.
        """
        
        if name == 'Beijing':
            return cls(name, 21500000)
        elif name == 'London':
            return cls(name, 9000000)
        elif name == 'New York':
            return cls(name, 8500000)
        elif name == 'São Paulo':
            return cls(name, 12000000)
        else:
            print('Sorry, this name is not in our database.\n')

    # Example of static method. Does not need a instance of the city
    # class to be called but does not have access to the class' parameters,
    # Usually used as an utils method for the class or application.
    @staticmethod
    def is_megalopolis(habitants):
        """
        Prints whether the city is a megalopolis.

        :param habitants: number of habitants of the city.
        :type habitants: int.
        :rtype: boolean.
        """

        if habitants <= 10000000:
            print("This city is not a megalopolis.\n")
        else:
            print("This city is a megalopolis.\n")

class Megalopolis(City):
    """
    Represents a megalopolis.

    """

    def __init__(self, name, habitants):
        """
        Creates a megalopolis.

        :param name: habitants of the megalopolis.
        :type name: string.
        :param habitants: number of habitants of the megalopolis.
        :type habitants: int.
        """

        super().__init__(name, habitants)

    # Implementation of the abstract method
    def age(self):
        """
        Prints megalopolis' age by its name. Only a few names are stored in the database

        """

        if self.name == 'Beijing':
            print('800 years old.\n')
        elif self.name == 'London':
            print('2000 years old.\n')
        elif self.name == 'New York':
            print('400 years old.\n')
        elif self.name == 'São Paulo':
            print('468 years old.\n')
        else:
            print('Sorry, this name is not in our database.\n')

##### Usage examples #####

# Creating City  and Megalopolis instances
hometown = City('Teresina', 1000000)
sjc = City('São José dos Campos', 700000)
london = Megalopolis('London', 9000000)

# Using abstract method
london.age()

# Using instance methods
hometown.print_name()
sjc.print_name()
london.print_name() # we can use City instance methods in child classes

hometown.change_name('Cidade Verde')
hometown.print_name()

# Using class method
rio = City.from_name('Rio de Janeiro') # We can use the method directly from the class,
sp = Megalopolis.from_name('São Paulo') # without an instance. It works for child classes too

sp.age() # Now we can use any instance method. Abstract methods too in case it is a child class
sp.change_name('Cidade Cinza')
sp.print_name() 

# Using static method
hometown.is_megalopolis(hometown.habitants) # Calling with an instance
sp.is_megalopolis(sp.habitants)
City.is_megalopolis(10000) # Calling without an instance