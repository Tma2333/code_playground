#!usr/bin/python3

class solution:
    def sol1(self, height):
        maxA = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                area = min(height[i], height[j])*(j-i)
                if area>maxA:
                    maxA = area
        return maxA

sol = solution()
ans = sol.sol1([1,3,3,1])
print(ans)