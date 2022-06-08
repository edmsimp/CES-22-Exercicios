from products.abstract.carrot_cake import CarrotCake

class BirthdayCarrotCake (CarrotCake):
    def __init__(self):
        super().__init__()
        print("Happy Birthday!!\n")