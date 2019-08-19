#!usr/bin/python3

class Solution:
    def search(self, nums, target):
        if not nums:
            return -1

        self.target = target
        self.nums = nums

        return self.binary_search(0, len(self.nums)-1)
    
    def binary_search (self, l, r):
        m = (l+r)//2
        print(l,m,r)
        if self.nums[m] == self.target:
            return m
        if r >= l:
            if ((self.target < self.nums[m] and self.nums[l] <= self.target < self.nums[m]) or 
                (self.target < self.nums[m] and self.nums[l] > self.nums[m]) or 
                (self.target > self.nums[m] and self.target >= self.nums[l] and self.target > self.nums[r] and self.nums[m] < self.nums[r])):
                return self.binary_search(l, m-1)
            else:
                return self.binary_search(m+1, r)
        else:
            return -1




sol = Solution()
nums = [4,5,6,7,8,1,2,3]
target = 8
print(sol.search(nums, target))