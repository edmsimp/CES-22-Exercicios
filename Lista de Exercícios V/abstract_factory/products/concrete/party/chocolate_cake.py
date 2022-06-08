from products.abstract.chocolate_cake import ChocolateCake

class PartyChocolateCake (ChocolateCake):
    def __init__(self):
        super().__init__()
        print("Happy party!!\n")