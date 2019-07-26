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

sol = solutions()
print(sol.sol1('aasdfasdb', '.*.*db'))


                
            