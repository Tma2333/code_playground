#!usr/bin/python3

class solutions:
    def sol1(self, s):
        if not s:
            return True
        
        ls = []

        for ch in s:
            if ch in ['(', '[', '{']:
                ls.append(ch)
            
            if ch in [')', ']', '}']:
                if ls == []:
                    return False
                a = ls.pop()
                if ch == ')' and a != '(':
                    return False
                elif ch == '}' and a != '{':
                    return False
                elif ch == ']' and a != '[':
                    return False

        if ls != []:
            return False

        return True
    
    def sol2 (self, s):
        if not s: 
            return True
        
        keymap = {'}':'{',
                  ']':'[',
                  ')':'('}

        stack = []
        
        for c in s:
            if c in keymap:
                a = stack.pop() if stack else '#'
                if a != keymap[c]:
                    return False
            else:
                stack.append(c)
        
        return not stack

sol = solutions()
print(sol.sol2('('))