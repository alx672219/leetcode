from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # build hash map : character and how often it appears
        count = Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):  #idx	2 , ch	"v"
            if count[ch] == 1:
                return idx     
        return -1