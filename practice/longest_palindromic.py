#!usr/bin/python3

class solutions:
    def sol1 (self, s):
        largest = 0
        index = [0,0]
        for i in range(len(s)):
            a = self.expand_middle(s, i, i)
            b = self.expand_middle(s, i, i+1)
            if a > largest:
                largest = a
                index = [i,i]
            if b > largest:
                largest = b
                index = [i, i+1]
        
        palindromic = s[index[0]-round(largest/2+0.01)+1:index[1]+round(largest/2+0.01)]
        return palindromic

    def expand_middle (self, s, L, R):
        if L == R:
            count = -1
        else:
            count = 0
        while (L>=0 and R<=len(s)-1 and s[L]==s[R]):
            L -= 1
            R += 1
            count += 2
        return count

def test():
    sol = solutions()
    s = sol.sol1('a')
    print(s)

test()