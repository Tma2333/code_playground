#!/usr/bin/python3

"""Problem
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
"""

class solutions:
    def sol1 (self, string):
        unique_list = []
        sub_str_len = 0
        for ch in string:
            if ch not in unique_list:
                unique_list.append(ch)
            else:
                unique_list = [ch]
            if len(unique_list) > sub_str_len:
                sub_str_len = len(unique_list)
        return sub_str_len

def test():
    sol = solutions()
    print(sol.sol1('abcabcbb'))
    print(sol.sol1('xxxxxxxxxx'))
    print(sol.sol1('pwwkew'))
    print(sol.sol1('asdfaffxzvdstgh'))

test()
