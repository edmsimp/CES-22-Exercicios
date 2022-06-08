from factories.abstract_factory import AbstractFactory
from products.concrete.wedding.chocolate_cake import WeddingChocolateCake
from products.concrete.wedding.manioc_cake import WeddingManiocCake
from products.concrete.wedding.carrot_cake import WeddingCarrotCake

class WeddingFactory (AbstractFactory) :

    def createChocolateCake(self):
        super().createChocolateCake()
        WeddingChocolateCake()

    def createManiocCake(self):
        super().createManiocCake()
        WeddingManiocCake()
    
    def createCarrotCake(self):
        super().createCarrotCake()
        WeddingCarrotCake()