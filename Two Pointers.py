from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            
        # header
        head = ListNode()
        out = head
        
        forwd = 0
        
        while l1 is not None and l2 is not None:
            
            cur = l1.val + l2.val + forwd
            
            if cur >= 10: 
                cur -= 10
                forwd = 1
            else:
                forwd = 0
                
            tmp = ListNode(val=cur, next=None)
            out.next = tmp
            out = out.next
            
            l1 = l1.next
            l2 = l2.next
            
        l3 = l1 if l1 is not None else l2
        
        while l3 is not None:
            
            cur = l3.val + forwd
            
            if cur >= 10: 
                cur -= 10
                forwd = 1
            else:
                forwd = 0
                
            tmp = ListNode(val=cur, next=None)
            out.next = tmp
            out = out.next
            
            l3 = l3.next
            
        if forwd == 1:
            
            tmp = ListNode(val=1, next=None)
            out.next = tmp
            out = out.next
            
        return head.next
            
        