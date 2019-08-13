#!usr/bin/python3

class solutions:
    def generateParenthesis(self, n: int):
        if not n:
            return []

        self.n = n 
        self.ans = []
        
        self.rec(1, 0, '', '(')

        return self.ans

    def rec(self, l, r, s, par):
        s += par

        if l == self.n and r == self.n:
            self.ans.append(s)
            return

        if l == self.n:
            self.rec(l, r+1, s, ')')
            return

        if l == r:
            self.rec(l+1, r, s, '(')
            return

        if l > r:
            self.rec(l+1, r, s, '(')
            self.rec(l, r+1, s, ')')
            return

ans = solutions()
print(ans.generateParenthesis(15))