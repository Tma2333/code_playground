#!usr/bin/python3

class Solution:
    def countAndSay(self, n: int) -> str:
        ans = '1'
        
        for _ in range(n-1):
            target = ans
            count, num = 0, target[0]
            prv = target[0]
            ans = ''
            for ch in target:
                if ch == prv:
                    count += 1
                    continue
                else:
                    ans += str(count) + num
                    num = ch
                    prv = ch 
                    count = 1
            ans += str(count) + num
            
        
        return ans

sol = Solution()
print(sol.countAndSay(5))
for i in range(1,11):
    print(sol.countAndSay(i))