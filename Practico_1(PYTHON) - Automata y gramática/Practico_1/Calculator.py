class Calculator:
    def __init__(self, string_value):
        self.__string = string_value

    def solve(self):
        return eval(self.__string)

string = Calculator("2 * 2 * 2 + 32 * 2")
print(string.solve())