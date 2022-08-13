from Transport import *
from Constants import *
ejecuted = True

while ejecuted:
    opc = int(input(OPC_INPUT))

    if opc == 1:
        bike = Bike(2022, "Trek", "Flash", 2, "Rojo")
        bike.load_bike()

    elif opc == 2:
        car = Car(2017, "Renault", "Megane 2", 4, 5)
        car.load_car()

    elif opc == 3:
        if len(bikes) > 0:
            bike.__str__()
        else:
            print("ERROR: NO HAY BICIS CARGADAS.\nCARGUE EN LA OPCIÓN 1")

    elif opc == 4:
        if len(cars) > 0:
            car.__str__()
        else:
            print("ERROR: NO HAY AUTOS CARGADOS.\nCARGUE EN LA OPCIÓN 2")

    elif opc == 5:
        ejecuted = False