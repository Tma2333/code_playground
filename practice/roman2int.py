#!usr/bin/python3

class solutions:
    def sol1(self, s):
        total = 0
        i = 0
        while i < len(s):
            if s[i] == 'M':
                total += 1000
            elif s[i] == 'D':
                total += 500
            elif s[i] == 'C':
                if i != len(s)-1 and s[i+1] == 'D':
                    total += 400
                    i += 2
                    continue
                elif i != len(s)-1 and s[i+1] == 'M':
                    total += 900
                    i += 2
                    continue
                else:
                    total += 100
            elif s[i] == 'L':
                total += 50
            elif s[i] == 'X':
                if i != len(s)-1 and s[i+1] == 'L':
                    total += 40
                    i += 2
                    continue
                elif i != len(s)-1 and s[i+1] == 'C':
                    total += 90
                    i += 2
                    continue
                else:
                    total += 10
            elif s[i] == 'V':
                total += 5
            elif s[i] == 'I':
                if i != len(s)-1 and s[i+1] == 'X':
                    total += 9
                    i += 2
                    continue
                elif i != len(s)-1 and s[i+1] == 'V':
                    total += 4
                    i += 2
                    continue
                else:
                    total += 1

            i += 1
        return total
    
    def sol2 (self, s):
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0

        for i in range(len(s)-1):
            if roman_dict[s[i]] >= roman_dict[s[i+1]]:
                total += roman_dict[s[i]]
            else:
                total -= roman_dict[s[i]]
        
        return total + roman_dict[s[-1]]


sol = solutions()
print(sol.sol2('LVIII'))