class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            a = target - num
            if a not in h:
                h[num] = i # index 저장
            else:
                return [h[a], i] #[a의 index, index]