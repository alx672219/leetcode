class Solution:
    def numSplits(self, s: str) -> int:
        # this is not neccessary, but speeds things up
        length = len(s)
        if length == 1:  # never splittable
            return 0
        elif length == 2:  # always splittable
            return 1
        
        total = 0
        
        # prefix unique count
        prefix_count = [0]*len(s)
        unique = set()
        for i in range(len(s)):
            unique.add(s[i])
            prefix_count[i] = len(unique)
        
        # checking suffix
        unique.clear()
        for j in range(len(s) - 1, 0, -1):
            unique.add(s[j])
            if prefix_count[j-1] == len(unique):
                total += 1
            
        return total        
