class Solution:
    def groupAnagrams(self, strs: List[str]):
        ans = collections.defaultdict(list) # defaultdict automatically provides a default value for keys that don't exist in the dictionary when accessed
        for s in strs:
            ans[tuple(sorted(s))].append(s) # ex) defaultdict(<class 'list'>, {('a', 'e', 't'): ['eat', 'tea'], ('a', 'n', 't'): ['tan']})
        return ans.values()