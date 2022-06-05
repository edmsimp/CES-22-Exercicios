from products.product import Product
from utils import BookTaxes

class Book(Product):

    def __init__(self, title, author, genre, ed, editor, s_price,  b_price):
        super().__init__(title, s_price,  b_price)
        self.author = author
        self.genre = genre
        self.ed = ed
        self.editor = editor
        self.taxes = self.get_taxes()


    def get_taxes(self):
        return BookTaxes().get_taxes(self.s_price, self.b_price, self.genre)#, self.genre)

