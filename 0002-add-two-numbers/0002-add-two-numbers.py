# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        carry = 0
        cur = head
        
        while l1 or l2:
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0
            
            added = l1_val + l2_val + carry
            cur.next = ListNode(added % 10)
            carry = added // 10
            cur = cur.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        if carry:
            cur.next = ListNode(carry)
        return head.next