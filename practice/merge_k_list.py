#!usr/bin/python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        if len(lists) > 1:
            mid = len(lists)//2
            l = lists[:mid]
            r = lists[mid:]

            l = self.mergeKLists(l)
            r = self.mergeKLists(r)

            cur = ListNode(None)
            sudo_head = cur
    
            while l != None or r != None:
                if l == None:
                    cur.next = r
                    break
                if r == None:
                    cur.next = l
                    break
    
                if l.val <= r.val:
                    cur.next = l
                    cur = cur.next
    
                    l = l.next
                elif r.val < l.val:
                    cur.next = r
                    cur = cur.next
                    
                    r = r.next

            return sudo_head.next
        elif len(lists) == 1:
            return lists[0]


