#!usr/bin/python

class solution:
    def sol1(self, strs):
        if not strs:
            return ''

        s = min(strs)
        pre_fix = ''
        for i in range(len(s)):
            ch = s[i]
            correct = 0
            for ss in strs:
                if ss[i] == ch:
                    correct += 1
            if correct == len(strs):
                pre_fix += ch
            else:
                return pre_fix
        return pre_fix

sol = solution()
print(sol.sol1(['']))
