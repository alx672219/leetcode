# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        curr = head
        while curr is not None:
            vals.append(curr.val)
            curr = curr.next
        return vals == vals[::-1] 
                       # reverse the list (order)