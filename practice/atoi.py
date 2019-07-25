#!usr/bin/python3

class solutions:
    def sol1(self, str):
        str = str.strip()
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        a = ''
        if len(str) == 0:
            return 0

        if str[0]=='-':
            sign = -1
            str = str [1:]    
        elif str[0]=='+':
            sign = 1
            str = str[1:]
        else:
            sign = 1

        for ch in str:
            if ch in '0123456789':
                a += ch
            else:
                break
        if a == '':
            return 0
        return max(min(int(a)*sign, INT_MAX), INT_MIN)

def test():
    sol = solutions()
    i = sol.sol1('-')
    print(i)

test()