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
    
    def sol2(self, height):
        maxA, left, right = 0, 0, len(height)-1
        while right > left:
            maxA = max(maxA, min(height[left], height[right])*(right-left))

            if height[left]>height[right]:
                right -= 1
            else:
                left += 1
        return maxA

sol = solution()
ans = sol.sol1([1,3,3,1,13,21,4,1,21,32,13,2,123,14,123,12,321,321,4,123,21,312,3,123,1,31,412,3,123,21,3123,12,312,31,4,12,3,23])
print(ans)
ans = sol.sol2([1,3,3,1,13,21,4,1,21,32,13,2,123,14,123,12,321,321,4,123,21,312,3,123,1,31,412,3,123,21,3123,12,312,31,4,12,3,23])
print(ans)