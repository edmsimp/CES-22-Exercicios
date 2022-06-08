from products.abstract.manioc_cake import ManiocCake

class PartyManiocCake (ManiocCake):
    def __init__(self):
        super().__init__()
        print("Happy party!!\n")