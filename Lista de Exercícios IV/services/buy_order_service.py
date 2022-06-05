from products.product import Product

class BuyOrderService:

    def insert(self, order_data, product):
        order_data.append(product)
        return product

    def modify(self, order_data, product):
        found = False
        for p in order_data:
            if product == p:
                found = True
                print("Order modified")
        if found == False:
            print("Order not found")

    def get(self, order_data, product):
        found = False
        for p in order_data:
            if product == p:
                found = True
                print("Order returned")
                return p
        if found == False:
            print("Order not found")

    def remove(self, order_data, product):
        found = False
        for p in order_data:
            if product == p:
                found = True
                print("Order removed")
                order_data.remove(p)
                return p
        if found == False:
            print("Order not found")
