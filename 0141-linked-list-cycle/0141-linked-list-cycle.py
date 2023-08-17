# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        slower = head
        faster = head.next
        
        while slower != faster:
            
            if slower is None or faster is None:
                return False
            if faster.next is None:
                return False
            slower = slower.next # Floyd's cycle은 항상 slower is 1 step, faster is 2 steps 외우자.
            faster = faster.next.next
            # If there is no cycle in the list, the fast pointer will eventually reach the end and we can return false in this case.
        
        return True