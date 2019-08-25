#!usr/bin/python3
class Solution:
    def firstMissingPositive(self, nums) -> int:
        n = len(nums)

        for i in range(n):
            while 0 < nums[i] <= n and i+1 != nums[i] and nums[nums[i]-1] != nums[i]:
                temp = nums[i]
                nums[i], nums[temp-1] = nums[temp-1], nums[i]
                
            print(nums)
        
        for i in range(n):
            if nums[i] != i+1:
                return i + 1
        return n+1