#!usr/bin/python3

class solutions:
    def sol1(self, nums):
        if len(nums) < 3:
            return []
        
        if max(nums) < 0:
            return []
        
        nums = sorted(nums)
        ans = []
        for i in range (len(nums)-2):
            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1
            r = len(nums)-1

            while (l<r):
                s = nums[i] + nums[l] + nums [r]
                if s<0:
                    l += 1
                elif s>0:
                    r -= 1
                else:
                    temp = [nums[i], nums[l], nums[r]]
                    ans.append(temp)
                    while l<r and nums[l]==nums[l+1]:
                        l += 1
                    while l<r and nums[r]==nums[r-1]:
                        r -= 1
                    l += 1
            
        return ans

            
            
sol = solutions()
print(sol.sol1([-1,-2,-3,0]))

