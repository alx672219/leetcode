class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        strs.sort()
        for x, y in zip(strs[0], strs[-1]):  # sort한 다음에 맨 첫번째거랑 마지막만 비교하면 가운데것들은 비교 안해도된다.
            if x == y:
                prefix +=x
            else: 
                break
        return prefix