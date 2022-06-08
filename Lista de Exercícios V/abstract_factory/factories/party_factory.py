from factories.abstract_factory import AbstractFactory
from products.concrete.party.chocolate_cake import PartyChocolateCake
from products.concrete.party.manioc_cake import PartyManiocCake
from products.concrete.party.carrot_cake import PartyCarrotCake

class PartyFactory (AbstractFactory) :

    def createChocolateCake(self):
        super().createChocolateCake()
        PartyChocolateCake()

    def createManiocCake(self):
        super().createManiocCake()
        PartyManiocCake()
    
    def createCarrotCake(self):
        super().createCarrotCake()
        PartyCarrotCake()