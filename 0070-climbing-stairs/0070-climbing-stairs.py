class Solution:
    def climbStairs(self, n: int) -> int:

        # number of stairs: 1 2 3 4 5 6 
        # how many ways:    1 2 3 5 8 13  ex) 13 = 8 + 5
        # this is fibonacci sequence
        
        if n <= 2:
            return n
        else:
            prev1 = 1
            prev2 = 2
            current = 0
            
            for i in range(2,n):
                current = prev1 + prev2
                prev1 = prev2
                prev2 = current
            return current
        