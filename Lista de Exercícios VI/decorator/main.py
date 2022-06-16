# Pizza builder using same template given in the slides

# Common interface for the objects and the decorator
class FoodComponent:
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost

# Concrete Component, the pizza
class Pizza(FoodComponent):
    cost = 0.0

# Decorators superclass
class Decorator(FoodComponent):
    def __init__(self, foodComponent):
        self.component = foodComponent

    def getTotalCost(self):
        return self.component.getTotalCost() + FoodComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + " " + FoodComponent.getDescription(self)

# Decorators implementation: the flavors and border options
class Pepperoni(Decorator):
    cost = 0.50
    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)

class Margherita(Decorator):
    cost = 0.75
    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)

class Chicken(Decorator):
    cost = 0.75
    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)

class Borders(Decorator):
    cost = 0.25
    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)

class NoBorders(Decorator):
    cost = 0.00
    def __init__(self, foodComponent):
        Decorator.__init__(self, foodComponent)

# Usage examples
margheritta_with_borders = Margherita(Borders(Pizza()))
print(margheritta_with_borders.getDescription()+ ": $" + str(margheritta_with_borders.getTotalCost()))
chicken_without_borders = Chicken(NoBorders(Pizza()))
print(chicken_without_borders.getDescription()+ ": $" + str(chicken_without_borders.getTotalCost()))