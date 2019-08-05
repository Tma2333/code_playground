#!usr/bin/python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return

        i, j = [0, head], [0, head]
        
        while i[1].next != None:
            if i[0] - j[0] == n:
                j[1] = j[1].next
                j[0] += 1
            
            i [1] = i[1].next
            i[0] += 1
        
        if n-1 == i[0]:
            head = head.next
        else:
            j[1].next = j[1].next.next

        return head


        
     
