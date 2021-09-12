import random

class roll_Gen:
    def gen(self, n, ch):
        roll = ""
        s_r = ""
        state = ""
        r = 0
        for i in range(12):
            r = random.randint( 0, 9)
            roll = roll + str(abs(r - n) % 5)

        roll[:12]

        if  (ch == '1'):
            s_r = "AP011-{}".format(roll)
            state = "Andhra Pradesh"
            return s_r, state
        elif (ch == '2'):
            s_r = "BH021-{}".format(roll)
            state = "Bihar"
            return s_r, state
        elif (ch == '3'):
            s_r = "MH013-{}".format(roll)
            state = "Maharashtra"
            return s_r, state
        elif (ch == '4'):
            s_r = "UP031{}".format(roll)
            state = "Uttar Pradesh"
            return s_r, state
        elif (ch == '5'):
            s_r = "WB014{}".format(roll)
            state = "West Bengal"
            return s_r, state
        else:
            return "NULL"