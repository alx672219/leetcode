class Solution:
    def reverseBits(self, n: int) -> int:
    
        # revs_number = 0 

        # # reverse the integer number using the while loop  
        # while (number > 0):  
        #     # Logic  
        #     remainder = number % 10  
        #     revs_number = (revs_number * 10) + remainder  
        #     number = number // 10  
        
        # return revs_number

        ret, power = 0, 31 # 32 bits
        while n:
            ret += (n & 1) << power
            n = n >> 1 # iterate from right to left
            power -= 1
        return ret