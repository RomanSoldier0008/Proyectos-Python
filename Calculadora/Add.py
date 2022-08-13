from Constants import RESULT, RESULT_EXTENSION

class Add:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add_and_return(self):
        return RESULT.format(self.num1 + self.num2) + RESULT_EXTENSION