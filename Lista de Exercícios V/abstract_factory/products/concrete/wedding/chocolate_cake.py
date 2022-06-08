from products.abstract.chocolate_cake import ChocolateCake

class WeddingChocolateCake (ChocolateCake):
    def __init__(self):
        super().__init__()
        print("Happy wedding!!\n")