from products.abstract.carrot_cake import CarrotCake

class PartyCarrotCake (CarrotCake):
    def __init__(self):
        super().__init__()
        print("Happy party!!\n")