from products.abstract.carrot_cake import CarrotCake

class WeddingCarrotCake (CarrotCake):
    def __init__(self):
        super().__init__()
        print("Happy wedding!!\n")