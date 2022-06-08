from products.abstract.chocolate_cake import ChocolateCake

class BirthdayChocolateCake (ChocolateCake):
    def __init__(self):
        super().__init__()
        print("Happy birthday!!\n")