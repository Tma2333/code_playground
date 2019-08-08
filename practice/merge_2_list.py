#!usr/bin/python3

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class solutions:
    def sol1(self, l1: ListNode, l2: ListNode):
        cur = None
        sudo_head = ListNode(None)
        sudo_head.next = cur

        while l1 != None and l2 != None:
            if l1 == None:
                cur = l2
            if l2 == None:
                cur = l1

            if l1.val <= l2.val:
                print(1)
                if cur:
                    cur.next = l1
                    cur = cur.next
                else:
                    cur = l1

                l1 = l1.next
            elif l2.val < l1.val:
                print(2)
                if cur:
                    cur.next = l2
                    cur = cur.next
                else:
                    cur = l2
                
                l2 = l2.next
        
        return sudo_head.next