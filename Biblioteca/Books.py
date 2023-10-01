from Constants import *
class Books:
    def __init__(self, nombre, autor, isbn):
        self.nombre = nombre
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return RETURN_BOOKS_FORMAT.format(self.nombre, self.autor, self.isbn)