from Constant import *

class String_calculator:
    def __init__(self):
        self.__string = ""
        self.__new_string = ""
        self.__total = 0

    def enter(self):
        self.__string = str(input(INPUT_STRING_INPUT))

    def delete_letter(self):
        for letter in self.__string:
            if letter.isnumeric() or letter == "+" or letter == "*" or letter == "-" or letter == "/":
                self.__new_string += letter

    def print(self):
        return self.__new_string

    def operate(self):
        self.__total = eval(self.__new_string)
        return self.__total