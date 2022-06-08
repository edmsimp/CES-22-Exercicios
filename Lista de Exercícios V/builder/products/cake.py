class Cake:

    def __init__(self):
        self.type = None
        self.style = None

    def set_type(self, type):
        self.type = type
        print("\nDelivering " + type + " cake!")

    def set_style(self, style):
        self.style = style
        print("Happy " + style +"!\n")