# External class to calculate the product taxes
class Taxes:

    def get_taxes(self, buy, sell):
        return (sell - buy)/10

# Book taxes calculator
class BookTaxes (Taxes):

    def get_taxes(self, buy, sell, genre="Drama"):
        if genre == "Drama":
            return super().get_taxes(buy, sell)*3
        else:
           return super(self).get_taxes(buy, sell)*5

# Print functionality for the orders
class OrderList:

    def print_order(self, product):
        a = product.s_price
        t = str(a)
        print("Buy title: " + product.title + " - " + t + " - 1 u")