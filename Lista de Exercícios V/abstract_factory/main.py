from factories.birthday_factory import BirthdayFactory
from factories.wedding_factory import WeddingFactory
from factories.party_factory import PartyFactory

class Client:
    def __init__(self, factory):
        self.factory = factory()

# Simulation
while(True):
    print("Hello client!")
    print("Describe the type of cake you want:")
    print("Disponible types: 1 - Chocolate, 2 - Manioc, 3 - Carrot")
    print("Disponible styles: 1 - Birthday, 2 - Wedding, 3 - Party")
    print("Press Ctrl + C in case you want to exit.")

    type = int(input("Type you want: "))
    style = int(input("Style you want: "))

    if type == 1:
        if style == 1:
            client = Client(BirthdayFactory)
            client.factory.createChocolateCake()
        elif style == 2:
            client = Client(WeddingFactory)
            client.factory.createChocolateCake()
        elif style == 3:
            client = Client(PartyFactory)
            client.factory.createChocolateCake()
        else:
            print("Invalid input")
    elif type == 2:
        if style == 1:
            client = Client(BirthdayFactory)
            client.factory.createManiocCake()
        elif style == 2:
            client = Client(WeddingFactory)
            client.factory.createManiocCake()
        elif style == 3:
            client = Client(PartyFactory)
            client.factory.createManiocCake()
        else:
            print("Invalid input")
    elif type == 3:
        if style == 1:
            client = Client(BirthdayFactory)
            client.factory.createCarrotCake()
        elif style == 2:
            client = Client(WeddingFactory)
            client.factory.createCarrotCake()
        elif style == 3:
            client = Client(PartyFactory)
            client.factory.createCarrotCake()
        else:
            print("Invalid input")
    else: 
        print("Invalid input")