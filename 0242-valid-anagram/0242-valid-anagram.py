from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)   # Counter is a container that will hold the count of each of                                 # the elements present in the container.