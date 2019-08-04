#!usr/bin/python3

class solutions:
    def sol1(self, digits):
        if not digits:
            return []

        self.dmap = {'2':['a', 'b', 'c'],
                     '3':['d', 'e', 'f'],
                     '4':['g', 'h', 'i'],
                     '5':['j', 'k', 'l'],
                     '6':['m', 'n', 'o'],
                     '7':['p', 'q', 'r','s'],
                     '8':['t', 'u', 'v'],
                     '9':['w', 'x', 'y', 'z']}
        self.ans = []

        self.combo(digits, 0, '')
        
        return self.ans

        
    
    def combo(self, digits, i, s):
        temp = s
        for ch in self.dmap[digits[i]]:
            s += ch

            if i == len(digits) - 1:
                self.ans.append(s)
            else:
                self.combo(digits, i+1, s)
            s = temp
    

sol = solutions()
print(sol.sol1('234'))
            
        
        
        
        
