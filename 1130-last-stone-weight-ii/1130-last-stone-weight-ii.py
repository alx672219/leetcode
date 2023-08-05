class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = ceil(stone_sum / 2)

        def dfs(i, total):   # recursively 하나씩 내려간다
            if total >= target or i == len(stones):      # when done iterating
                return abs(total - (stone_sum - total))   # half - other half
            
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i])) 
                                    # either include the stone or don't
            return dp[(i, total)]

        dp = {}
        return dfs(0, 0)