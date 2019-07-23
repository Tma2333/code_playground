#!usr/bin/python3

class solutions:
    def sol1(self, x):
        x = str(x)
        a = ""
        for i in range(-1, -len(x)-1, -1):
            a += x[i]
        if a[-1] == '-':
            a = -int(a[:-1])
        else:
            a = int(a)
        if (a&0x7fffffff) not in (a, 0x80000000+a):
            return 0
        return a

    def sol2(self, x):
        rev = 0
        sign = 1
        if x<0:
            x = -x
            sign = -1
        while (x > 0):
            rev = rev*10+x%10
            x = x//10
        if (rev&0x7fffffff) not in (rev, 0x80000000+rev):
            return 0
        return rev * sign


    
def test():
    sol = solutions()
    x = sol.sol2(-123)
    print(x)

test()        
