OPC_INPUT = """
      MENÚ
-----------------
1) Cargar libro
2) Cargar cliente
3) Mostrar libros
4) Mostrar clientes
5) Dar libro a cliente
6) Mostrar libros asignados
7) Salir
-----------------
Ingrese opción del menú: """
CLIENT_NUMBER = "Cliente número: {}\n"
BOOK_NUMBER = "Libro número: {}\n"
BOOK_ADD_CLIENT = "{}\nAsignado al cliente: {}"
BOOK_LOAD_CLIENT = "Éxito al asignar"
# CLIENTE

RETURN_CLIENTS_FORMAT = """
*********
 CLIENTE
*********
Nombre: {}
Edad: {}
Direccion: {}"""
NAME_CLIENT_INPUT = "Ingrese nombre del cliente: "
AGE_CLIENT_INPUT = "Ingrese edad del cliente: "
ADDRESS_CLIENT_INPUT = "Ingrese direccion del cliente: "
LOADED_CLIENT = "CLiente cargado al sistema"
SELECTION_CLIENT_INPUT = "Seleccione el cliente: "

# LIBRO

LOADED_BOOK = "Libro cargado al sistema"
RETURN_BOOKS_FORMAT = """
*******
 LIBRO
*******
Nombre: {}
Autor: {}
ISBN: {}"""
NAME_BOOK_INPUT = "Ingrese nombre del libro: "
AUTOR_BOOK_INPUT = "Ingrese autor: "
ISBN_BOOK_INPUT = "Ingrese ISBN: "
SELECTION_BOOK_INPUT = "Seleccione el libro: "

# ERRORES O EXCEPCIONES

OPC_ERROR = "Error: Ingresaste mal la opcíon del menú"