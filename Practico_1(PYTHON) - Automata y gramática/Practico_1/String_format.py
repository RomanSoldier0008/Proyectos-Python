class String_format:
    def __init__(self, string_value):
        self.__string = string_value

    def validate_string(self):
        print(self.validate_1())
        print(self.validate_2())
        print(self.validate_3())
        print(self.validate_4())
        print(self.validate_5())
        print(self.validate_6())

    def validate_1(self):
        for letter in self.__string:
            if letter.isalnum():
                return letter.isalnum()
        return False

    def validate_2(self):
        for letter in self.__string:
            if letter.isalpha():
                return letter.isalpha()
        return False

    def validate_3(self):
        for letter in self.__string:
            if letter.isupper():
                return letter.isupper()
        return False

    def validate_4(self):
        for letter in self.__string:
            if letter.islower():
                return letter.islower()
        return False

    def validate_5(self):
        for letter in self.__string:
            if letter.isdigit():
                return letter.isdigit()
        return False

    def validate_6(self):
        if len(self.__string) >= 8:
            return True
        return False

string = String_format("xy@z!")
string.validate_string()