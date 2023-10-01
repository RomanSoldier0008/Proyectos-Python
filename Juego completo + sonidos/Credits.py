from constant import *
from time import sleep

class Credits:
    def __init__(self):
        self.ops = [CREDITS_PRINT, UNIVERSITY, THANKS, TEACHER1, TEACHER2, OP2_CREDIT, OP3_CREDIT, OP1_CREDIT, THANKS_BYE]

    def view_credits(self):
        count = 0
        space = "                                                   "
        for credit in self.ops:
            print(space + credit)
            if count != 8:
                sleep(4)
            else:
                sleep(6)
            count += 1