#!usr/bin/python3 

class Solution:
    def removeDuplicates(self, nums) -> int:
        p = 0

        for num in nums:
            if num != nums[p]:
                nums[p+1] = num
                p += 1
            
        return p+1
                