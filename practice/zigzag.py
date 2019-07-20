#!usr/bin/python3

class solution:
    def sol1(self, s, num_row):
        zigzag = ''
        if num_row == 1:
            return s
        for i in range (num_row):
            if len(zigzag) == len(s):
                break
            index = i
            row_factor = i*2
            factor1 = 0+row_factor
            factor2 = num_row*2-2-row_factor
            while True:
                if factor2 > 0:
                    zigzag += s[index]
                    index += factor2
                    if index >= len(s):
                        break
                if factor1 > 0:
                    zigzag += s[index]
                    index += factor1
                    if index >= len(s):
                        break

        return zigzag
    
    def sol2(self, s, numRows):
        zigzag = ''
        if numRows == 0 or 1:
            return s
        
        for i in range(numRows):
            


def test():
    sol = solution()
    zigzag = sol.sol1('a', 2)
    print(zigzag)

test() 