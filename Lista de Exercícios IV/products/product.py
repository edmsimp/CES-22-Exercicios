from utils import Taxes

# Main class to describe products, the other ones in this folder are children
# classes for each product.
class Product:

    def __init__(self, title, s_price, b_price):
        self.title = title
        self.s_price = s_price
        self.b_price = b_price
    
    def get_taxes(self, s_price, b_price):
        Taxes().get_taxes(s_price, b_price)