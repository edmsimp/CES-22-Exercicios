from factories.abstract_factory import AbstractFactory
from products.concrete.birthday.chocolate_cake import BirthdayChocolateCake
from products.concrete.birthday.manioc_cake import BirthdayManiocCake
from products.concrete.birthday.carrot_cake import BirthdayCarrotCake

class BirthdayFactory (AbstractFactory) :

    def createChocolateCake(self):
        super().createChocolateCake()
        BirthdayChocolateCake()

    def createManiocCake(self):
        super().createManiocCake()
        BirthdayManiocCake()
    
    def createCarrotCake(self):
        super().createCarrotCake()
        BirthdayCarrotCake()