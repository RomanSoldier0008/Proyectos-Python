from Constant import *
from String_calculator import String_calculator

class Main:
    def __init__(self, option_value=0):
        self.__option = option_value

    def start(self):
        while self.__option != EXIT:
            self.print(MAIN_MENU_OUTPUT)
            self.enter_option()
            self.choose_option(self.__option)
        self.print(GREETING_EXIT)

    def enter_option(self):
        try:
            self.__option = int(input(INPUT_MENU_OPTION))
        except ValueError:
            self.print(VALUE_ERROR)

    def print(self, print_value):
        print(print_value)

    def calculate_string(self):
        string_calculator = String_calculator()
        string_calculator.enter()
        string_calculator.delete_letter()
        self.print(string_calculator.print())
        self.print(string_calculator.operate())

    def choose_option(self, option):
        if option == 1:
            self.calculate_string()

menu = Main()
menu.start()