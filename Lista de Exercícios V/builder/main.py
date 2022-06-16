from director import Director
from builders.cake_builder import CakeBuilder


# The builder is specified to build cakes, then the director will command
# which cake has to be build 
builder = CakeBuilder()

director = Director()
director.builder = builder

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
            director.make_birthday_chocolate_cake()
        elif style == 2:
            director.make_wedding_chocolate_cake() 
        elif style == 3:
            director.make_party_chocolate_cake()
        else:
            print("Invalid input")
    elif type == 2:
        if style == 1:
            director.make_birthday_manioc_cake()
        elif style == 2:
            director.make_wedding_manioc_cake()
        elif style == 3:
            director.make_party_manioc_cake()
        else:
            print("Invalid input")
    elif type == 3:
        if style == 1:
            director.make_birthday_carrot_cake()
        elif style == 2:
            director.make_wedding_carrot_cake()
        elif style == 3:
            director.make_party_carrot_cake()
        else:
            print("Invalid input")
    else: 
        print("Invalid input")