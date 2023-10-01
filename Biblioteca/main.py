from Library import *
from Constants import *
ejecuted = True

while ejecuted:
    opc = int(input(OPC_INPUT))

    if opc == 1:
        Library().load_books()
    elif opc == 2:
        Library().load_clients()
    elif opc == 3:
        Library().view_books()
    elif opc == 4:
        Library().view_clients()
    elif opc == 5:
        Library().add_book_to_client()
    elif opc == 6:
        Library().view_books_to_clients()
    elif opc == 7:
        ejecuted = False
    else:
        print(OPC_ERROR)