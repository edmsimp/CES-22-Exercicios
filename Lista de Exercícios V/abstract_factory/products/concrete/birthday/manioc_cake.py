from products.abstract.manioc_cake import ManiocCake

class BirthdayManiocCake (ManiocCake):
    def __init__(self):
        super().__init__()
        print("Happy Birthday!!\n")