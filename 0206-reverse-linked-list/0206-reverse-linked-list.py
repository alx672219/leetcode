# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:                                                 # 1 -> 2 -> 3 -> None
            next_temp = curr.next   # Remember next node.           # next_temp = 2 -> 3 ->
            curr.next = prev   # REVERSE! None, first time round.   # None <- 1 2 -> 3 ->
            prev = curr   # Used in the next iteration.             # prev = 1
            curr = next_temp   # Move to next node.                 # curr = 2
            
        return prev