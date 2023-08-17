# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next is not None: 
            num = num * 2 + head.next.val
            head = head.next
        return num
    
    # 규칙 외우자
    # ex) 1011
    # 1 x 2^4 + 0 x 2^3 + 0 x 2^2 + 1 x 2^1 + 1 x 2^0
    # = 1x2+0 = 2
    #           2x2+0 = 4
    #                   4x2+1 = 9
    #                           9x2+1 = 18