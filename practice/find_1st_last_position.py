#!usr/bin/python3

class Solution:
    def searchRange(self, nums, target):
        def binary_search(l, r, nums, target):
            m = (l+r)//2

            if r >= l:
                if nums[m] == target:
                    return m
                
                if nums[m] > target:
                    return binary_search(l, m-1, nums, target)
                else:
                    return binary_search(m+1, r, nums, target)
            
            else:
                return -1

        i = binary_search(0, len(nums)-1, nums, target)
        ans = [i,i]

        if ans == [-1, -1]:
            return ans
        
        while ans[0] != 0 and nums[ans[0]-1] == target:
            ans[0] -= 1
        
        while ans[1] != len(nums)-1 and nums[ans[1]+1] == target:
            ans[1] += 1
        
        return ans


sol = Solution()
nums = [1,2,3,4,5,7,8]
target = 6
print(sol.searchRange(nums, target))
