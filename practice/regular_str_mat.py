#!usr/bin/python3

class solutions:
    def sol1(self, s, p):
        if s == '' and p == '':
            return True
        elif s == '' and p != '':
            return False
        
        hold = False
        j = 0
        for i in range(len(p)):
            strA = p[i]
            strB = s[j]
            print(strA+' '+strB)

            if strA == '*':
                if i == 0:
                    return False
                strA = p[i-1]
                hold = True
            
            while hold:
                print('*'+strA+' '+strB)
                if strA in (strB, '.'):
                    j += 1
                    if j == len(s):
                        j = len(s)-1
                        break
                    strB = s[j]
                else:
                    break
            
            if hold:
                hold = False
                continue
            
            if strA not in (strB, '.') and p[i+1]!='*':
                return False    
            elif strA not in (strB, '.') and p[i+1] == '*':
                continue

            j += 1 
            if j == len(s):
                j =  len(s)-1
        
        if j < len(s)-1:
            return False
        return True

    def isMatch(self, s, p):
        if not p:
            return not s
        
        match = bool(s) and p[0] in {s[0], '.'}

        if len(p) >= 2 and p[1] == '*':
            return match or self.isMatch(s, p[2:]) and self.isMatch(s[1:], p)
        
        return match and self.isMatch(s[1:], p[1:])


sol = solutions()
print(sol.isMatch('a', 'ab'))


                
            