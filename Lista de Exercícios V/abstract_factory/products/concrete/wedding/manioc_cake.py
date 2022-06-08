from products.abstract.manioc_cake import ManiocCake

class WeddingManiocCake (ManiocCake):
    def __init__(self):
        super().__init__()
        print("Happy wedding!!\n")