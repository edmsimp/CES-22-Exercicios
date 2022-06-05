from products.book import Book
from services.service import Service

class BookService (Service) :

    def insert (self, book_data, title, author, genre, ed, editor, s_price,  b_price) :
        # create a new book and stores it
        new_book = Book (title, author, genre, ed, editor, s_price,  b_price)
        author.books_published.append (title)
        book_data.append (new_book)
        return new_book

    def modify(self, book_data, author, title):
        # search through the database with the author and title
        book = ''
        if (title == ""):
            print("No title gived, choose between one of them:")
            for author_book in author.books_published:
                print(author_book.title)
            book = input()
        else:
            book = title
        found = False
        for author_book in author.books_published:
            if book == author_book.title:
                found = True
                print("Book modified")  
                # TODO: add modify logic
                return title  
        if found == False:
            print("Invalid book, exiting service")
                    

    def get(self, book_data, author, title):
        book = ''
        if (title == ""):
            print("No title gived, choose between one of them:")
            for author_book in author.books_published:
                print(author_book.title)
            book = input()
        else:
            book = title
        found = False
        for author_book in author.books_published:
            if book == author_book.title:
                found = True
                print("Book returned")
                return book
        if found == False:
            print("Invalid book, exiting service")
            

    def remove(self, book_data, author, title):
        book = ''
        if (title == ""):
            print("No title gived, choose between one of them:")
            for author_book in author.books_published:
                print(author_book.title)
            book = input()
        else:
            book = title
        found = False
        for author_book in author.books_published:
            if book == author_book.title:
                found = True
                print("Book removed")
                book_data.remove(author_book)
                return author_book
        if found == False:
            print("Invalid book, exiting service")
