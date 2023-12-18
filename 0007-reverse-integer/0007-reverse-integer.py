class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            res=int(str(x)[::-1])
        else:
            res=int("-"+str(abs(x))[::-1])
        if res>=-2147483648 and res<=2147483647: #Check if the reversed integer falls within the acceptable 32-bit integer range i.e., [-2^31, 2^31-1].
            return res
        else:
            return 0
        