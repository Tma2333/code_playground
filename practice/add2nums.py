#!usr/bin/python3
"""Problem
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

class list_node:
    def __init__(self, num):
        self.num = num
        self.next = None


def list_gen(num):
    num = str(num)
    head = None
    for x in num:
        tem = list_node(int(x))
        tem.next = head
        head = tem
    
    return head

class solutions:
    def sol1 (self, num1, num2):
        carry = 0
        head = list_node(0)
        cur = head
        while True:
            if not num1 == None:
                x = num1.num
            else:
                x = 0

            if not num2 == None:
                y = num2.num
            else:
                y = 0
            
            s = x+y+carry
            carry = s//10
            new = list_node(s%10)
            cur.next = new
            cur = new 

            if num1 == None and num2== None:
                break

            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next
            
        return head.next

    def extract (self, node):
        i = 0
        num = 0
        while True:
            num += node.num*(10**i)
            if node.next == None:
                break
            node = node.next
            i += 1
        return num

    def sol2 (self, num1, num2):
        n1 = self.extract(num1)
        n2 = self.extract(num2)
        result = n1+n2
        
        return list_gen(result)

        
def test():
    num1 = list_gen(90)
    num2 = list_gen(10)
    sol = solutions()
    result = sol.sol1(num1, num2)
    result = sol.extract(result)
    print (result)

test()

