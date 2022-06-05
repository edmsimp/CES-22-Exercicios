from agents.client import Client
from agents.author import Author 
from products.book import Book
from services.book_service import BookService
from services.client_service import ClientService
from services.buy_order_service import BuyOrderService
from utils import *

# pseudo database
clients = []
authors = []
orders = []
books = []

# Initial variables, juts for test and examples
fultano = Author("Fultano", "fultano@gmail.com")
authors.append(fultano)

book = Book("Medieval Tales", fultano, "Drama", 3, "CostaSM", 100, 50)
books.append(book)

fultano.books_published.append(book)

admin_login = "admin"
admin_email = "admin@email.com"

clients.append(Client(admin_login, admin_email))

# Test booleans
is_admin = False
running = False

# Program loop. It was decided to do everything at main.py in order to simplify the project
# Very basic logic, the important part is the SOLID principles that were aplied on the others
# folders.
while True:
    print("\nWelcome to the bookshop. Login to use the platform. To exit, press Ctrl + C.")
    user_login = input("Enter your login username: ")
    user_email= input("Enter your email: ")
    for user in clients:
        if user.name == user_login:
            print("Welcome back, " + user_login + "\n")
            running = True
            if user_login == "admin":
                is_admin = True
                print("Entering Admin Mode\n")
            break
    else:
        print("Welcome " + user_login)
        user = ClientService().insert(clients, user_login, user_email)
        running = True
    while running:
        if is_admin:
            print(user_login + ", type the subject you want to access:\n")
            print("1 - books, 2 - clients, 3 - buy orders, 4 - exit")
            option = input()
            if option == "1":
                print("Disponible books:")
                for b in books:
                    print(b.title + ", " + b.author.name + ", " + str(b.ed) + " " + b.editor)
                    print("Price: " + str(b.s_price))
                print("Select an option:")
                print("1 - search, 2 - modify, 3 - add, 4 - remove")
                option_aux = input()
                if option_aux == "1":
                    a = input("Author: ")
                    t = input("Title (Press Enter to show book list): ")
                    author_search = ""
                    for author in authors:
                        if a == author.name:
                            author_search = author
                    if author_search != "":
                        book = BookService().get(books, author_search, t)
                    else:
                        print("Invalid author")
                elif option_aux == "2":
                    a = input("Author: ")
                    t = input("Title (Press Enter to show book list): ")
                    author_search = ""
                    for author in authors:
                        if a == author.name:
                            author_search = author
                    if author_search != "":
                        book = BookService().modify(books, author_search, t)
                    else:
                        print("Invalid author")
                elif option_aux == "3":
                    t = input("Title: ")
                    a = input("Author: ")
                    g = input("Gender: ")
                    ed = int(input("Edition: "))
                    e = input("Editor: ")
                    s = int(input("Sell Price: "))
                    b = int(input("Buy Price: "))
                    author_search = ""
                    for author in authors:
                        if a == author.name:
                            author_search = author
                    if author_search != "":
                        book = BookService().insert(books, t, author_search, g, ed, e, s, b)
                        author_search.books_published.append(book)
                        authors.append(author_search)
                    else:
                        print("Invalid author")
                elif option_aux == "4":
                    a = input("Author: ")
                    t = input("Title (Press Enter to show book list): ")
                    author_search = ""
                    for author in authors:
                        if a == author.name:
                            author_search = author
                            book = BookService().remove(books, author, t)
                    if author_search == "":
                        print("Invalid author")
                else: 
                    print("Invalid option")
            elif option == "2":
                print("Disponible clients:")
                for c in clients:
                    print(c.name + ", " + c.email)
                print("Select an option:")
                print("1 - search, 2 - modify, 3 - add, 4 - remove")
                option_aux = input()
                if option_aux == "1":
                    n = input("Name: ")
                    c = ClientService().get(clients, n)
                elif option_aux == "2":
                    n = input("Name: ")
                    c = ClientService().modify(clients, n)
                elif option_aux == "3":
                    n = input("Name: ")
                    e = input("Email: ")
                    client = ClientService().insert(clients, n, e)
                elif option_aux == "4":
                    n = input("Name: ")
                    c = ClientService().remove(clients, n)
            elif option == "3":
                print("Disponible orders:")
                for o in orders:
                    print(o.title + ", " + str(o.s_price))
                print("Select an option:")
                print("1 - search, 2 - modify, 3 - add, 4 - remove")
                option_aux = input()
                if option_aux == "1":
                    o = input("Order name: ")
                    for order in orders:
                        if order.name == o:
                            BuyOrderService().get(orders, order)
                elif option_aux == "2":
                    o = input("Order name: ")
                    for order in orders:
                        if order.name == o:
                            BuyOrderService().modify(orders, order)
                elif option_aux == "3":
                    n = input("Name: ")
                    e = input("Email: ")
                    client = ClientService().insert(clients, n, e)
                elif option_aux == "4":
                    o = input("Order name: ")
                    for order in orders:
                        if order.name == o:
                            BuyOrderService().remove(orders, order)
            elif option == "4":
                running = False
            else:
                print("invalid option\n")
        else:
            print(user_login + ", type the subject you want to access:\n")
            print("1 - books, 2 - exit")
            option = input()
            if option == "1":
                print("Disponible books:")
                for b in books:
                    print(b.title + ", " + b.author.name + ", " + str(b.ed) + " " + b.editor)
                    print("Price: " + str(b.s_price))
                print("Select an option:")
                print("1 - search, 2 - buy")
                option_aux = input()
                if option_aux == "1":
                    a = input("Author: ")
                    t = input("Title (Press Enter to show book list): ")
                    author_search = ""
                    for author in authors:
                        if a == author.name:
                            author_search = author
                    if author_search != "":
                        book = BookService().get(books, author_search, t)
                    else:
                        print("Invalid author")
                elif option_aux == "2":
                    a = input("Author: ")
                    t = input("Title (Press Enter to show book list): ")
                    for author in authors:
                        if a == author.name:
                            author_search = author
                    book = BookService().remove(books, author_search, t)
                    user.past_orders[book.title] = '1'
                    orders.append(book)
                    OrderList().print_order(book)
                else: 
                    print("Invalid option")               
            elif option == "2":
                running = False
            else:
                print("Invalid option\n")
