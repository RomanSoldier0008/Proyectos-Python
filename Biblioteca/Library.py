from Books import *
from Clients import *
books = []
clients = []
diccionary = {}

class Library:

    def load_books(self):
        name_book = str(input(NAME_BOOK_INPUT)).strip().title()
        autor_book = str(input(AUTOR_BOOK_INPUT)).strip().title()
        isbn_book = str(input(ISBN_BOOK_INPUT)).strip()
        book = Books(name_book, autor_book, isbn_book)
        books.append(book)
        print(LOADED_BOOK)

    def load_clients(self):
        name_client = str(input(NAME_CLIENT_INPUT)).strip().title()
        age_client = int(input(AGE_CLIENT_INPUT))
        address_client = str(input(ADDRESS_CLIENT_INPUT)).strip().title()
        client = Clients(name_client, age_client, address_client)
        clients.append(client)
        print(LOADED_CLIENT)

    def view_books(self):
        count = 0
        for book in books:
            count += 1
            print(BOOK_NUMBER.format(count), book)

    def view_clients(self):
        count = 0
        for client in clients:
            count += 1
            print(CLIENT_NUMBER.format(count), client)

    def add_book_to_client(self):
        global client, selection_client
        if len(books) > 0 and len(clients) > 0:
            for client in clients:
                print(client.nombre)
            selection_client = str(input(SELECTION_CLIENT_INPUT)).strip().title()
            for client in clients:
                if selection_client == client.nombre:
                    for book in books:
                        print(book.nombre)
                    selection_book = str(input(SELECTION_BOOK_INPUT)).strip().title()
                    for book in books:
                        if book.nombre == selection_book:
                            diccionary[client] = book
                            print(BOOK_LOAD_CLIENT)

    def view_books_to_clients(self):
        for i in diccionary:
            print(BOOK_ADD_CLIENT.format(diccionary[client], selection_client))