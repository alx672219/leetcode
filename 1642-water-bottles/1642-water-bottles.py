class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while (numBottles >= numExchange):
            remainder = numBottles % numExchange
            numBottles //= numExchange   # numBottles = numBottles / numExchange
            ans += numBottles
            numBottles += remainder

        return ans