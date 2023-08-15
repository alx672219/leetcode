class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashmap
        counts = collections.Counter(nums) # counts = Counter({숫자: 개수, 숫자: 개수, ...})
        return max(counts.keys(), key=counts.get)  # For key 2, counts.get(2) returns 개수.