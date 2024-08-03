# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tail = dummy = ListNode()
        carry = 0   # 8 + 6 = 14, carry is 1
        while l1 or l2:
            val1, val2 = 0, 0
            # iterate through each nodes
            if l1: 
                val1, l1 = l1.val, l1.next
            if l2: 
                val2, l2 = l2.val, l2.next
            
            val = carry + val1 + val2
            carry = val // 10   # 8 + 6 = 14, carry = 1
            val = val % 10      # 8 + 6 = 14, val = 4
            tail.next = ListNode(val)
            tail = tail.next
            
        if carry:
            tail.next = ListNode(carry) # set list node to next val and set it to 1
        head = dummy.next
        return head 
