from Constants import OPC_INPUT, NUM_INPUT, ERROR
from Add import Add
from Subtraction import Subtraction
from Multiplication import Multiplication
from Division import Division

ejecuted = True

def loaded_numbers():
    global num1, num2
    num1 = int(input(NUM_INPUT))
    num2 = int(input(NUM_INPUT))

while ejecuted:
    opc = int(input(OPC_INPUT))
    if 5 > opc >= 1:
        loaded_numbers()

    if opc == 1:
        object_add = Add(num1, num2)
        print(object_add.add_and_return())

    elif opc == 2:
        object_subtraction = Subtraction(num1, num2)
        print(object_subtraction.subtract_and_return())

    elif opc == 3:
        object_multiplication = Multiplication(num1, num2)
        print(object_multiplication.multiply_and_return())

    elif opc == 4:
        object_division = Division(num1, num2)
        print(object_division.divide_and_return())

    elif opc == 5:
        ejecuted = False

    else:
        print(ERROR)
        continue