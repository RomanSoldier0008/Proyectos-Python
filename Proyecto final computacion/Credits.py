from constant import *
from time import sleep

ops = [CREDITS_PRINT, UNIVERSITY, THANKS, TEACHER1, TEACHER2, OP2_CREDIT, OP3_CREDIT, OP1_CREDIT, THANKS_BYE]

class Credits:

    def view_credits(self):
        count = 0
        space = "                                                                                                      "
        for credit in ops:
            print(space + credit)
            if count != 8:
                sleep(4)
            else:
                sleep(6)
            count += 1