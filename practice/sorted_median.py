#!/usr/bin/python3

"""Problems

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
""" 

class solutions:
    def sol1(self, l1, l2):
        middle = (len(l1)+len(l2))//2
        a = len(l1)//2
        b = middle - a - 1
        print(a,b)
        l3 = []
        while True: 
            l3 = l1[:a+1]+l2[:b+1]
            print(l3)
            if a == len(l1)-1:
                b = min(middle -a - 1, len(l2)-1)
                break
            if b == len(l2)-1:
                a = min(middle - b - 1, len(l1)-1)
                break
            if l1[a]>l2[b+1]:
                a = a//2
                b = min(middle -a - 1, len(l2)-1)
                if a + b + 1 < middle:
                    a = min(middle - b - 1, len(l1)-1)
                    break
            elif l2[b]>l1[a+1]:
                b = b//2
                a = min(middle - b - 1, len(l1)-1)
                if a + b + 1 < middle:
                    b = min(middle -a - 1, len(l2)-1)
                    break
            else:
                break

            
        l3 = l1[:a+1]+l2[:b+1]
        print(l3)
        if (len(l1)+len(l2))%2:
            return max(l3)
        else:
            max1 = max(l3)
            l3.remove(max(l3))
            max2 = max(l3)
            return (max1+max2)/2
            

            
            
        
        


        
    
def test():
    l1 = [4,5,6,7,10,12,13,15,16,19]
    l2 = [1,2,3,14,15,43,56,54,234]        
    sol = solutions()
    print(sol.sol1(l1, l2))

test()

