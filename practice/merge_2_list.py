#!usr/bin/python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class solutions:
    def sol1(self, l1: ListNode, l2: ListNode):
        cur = ListNode(None)
        sudo_head = cur

        while l1 != None or l2 != None:
            if l1 == None:
                cur.next = l2
                break
            if l2 == None:
                cur.next = l1
                break

            if l1.val <= l2.val:
                cur.next = l1
                cur = cur.next

                l1 = l1.next
            elif l2.val < l1.val:
                cur.next = l2
                cur = cur.next
                
                l2 = l2.next

        return sudo_head.next