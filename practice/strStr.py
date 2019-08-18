#!usr/bin/python3

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle or not needle:
            return 0
        

        for i in range(len(haystack)):
            if needle[0] == haystack[i]:
                for j in range(len(needle)):
                    if len(needle) > len(haystack[i:]) or needle[j] != haystack[i:][j]:
                        break
                    if j == len(needle)-1:
                        return i
            
        return -1