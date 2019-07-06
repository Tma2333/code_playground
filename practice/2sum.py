#!usr/bin/python3

"""Problem:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class solutions:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def brute_force(self):
        result = []
        for i in range(len(self.nums)):
            for j in range(i+1, len(self.nums)):
                if self.nums[i] + self.nums[j] == self.target:
                    result.append(i)
                    result.append(j)
        return result


def test():
    nums = [1,6,9,7,14,3]
    target = 12
    sol = solutions(nums, target)
    print(sol.brute_force())

test()