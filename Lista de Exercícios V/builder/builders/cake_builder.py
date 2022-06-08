from builders.builder import Builder
from products.cake import Cake

class CakeBuilder (Builder):

    def reset(self):
        self.cake = Cake()

    def prepare_cake_type(self, type):
        self.reset()
        self.cake.set_type(type)

    def prepare_cake_style(self, style):
        self.reset()
        self.cake.set_style(style)