from builders.builder import Builder

class Director:

    def __init__(self):
        self.builder = None

    def builder(self, builder: Builder):
        self.builder = builder

    def make_birthday_chocolate_cake(self):
        self.builder.prepare_cake_type("chocolate")
        self.builder.prepare_cake_style("birthday")

    def make_birthday_manioc_cake(self):
        self.builder.prepare_cake_type("manioc")
        self.builder.prepare_cake_style("birthday")

    def make_birthday_carrot_cake(self):
        self.builder.prepare_cake_type("carrot")
        self.builder.prepare_cake_style("birthday")

    def make_wedding_chocolate_cake(self):
        self.builder.prepare_cake_type("chocolate")
        self.builder.prepare_cake_style("wedding")
    
    def make_wedding_manioc_cake(self):
        self.builder.prepare_cake_type("manioc")
        self.builder.prepare_cake_style("wedding")

    def make_wedding_carrot_cake(self):
        self.builder.prepare_cake_type("carrot")
        self.builder.prepare_cake_style("wedding")

    def make_party_chocolate_cake(self):
        self.builder.prepare_cake_type("chocolate")
        self.builder.prepare_cake_style("party")
    
    def make_party_manioc_cake(self):
        self.builder.prepare_cake_type("manioc")
        self.builder.prepare_cake_style("party")

    def make_party_carrot_cake(self):
        self.builder.prepare_cake_type("carrot")
        self.builder.prepare_cake_style("party")