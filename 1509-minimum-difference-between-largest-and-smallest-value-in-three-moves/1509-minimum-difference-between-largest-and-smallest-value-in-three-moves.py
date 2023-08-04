class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        minimum = max(nums)

        if nums[0] == nums[n - 1]:
            return 0      # 맨 첫번째거랑 마지막거랑 같으면 difference가 0
        
        if n < 5:
            return 0      # 3번 바꿀 수 있는데 4개의 숫자가 있으면 그중에서 3개를 다 바꾸면 다 같게 된다

        return min({nums[n - 1] - nums[3], nums[n - 2] - nums[2], nums[n - 3] - nums[1], nums[n - 4] - nums[0]})
                   
        # kill 3 smallest elements = A[n-4] - A[0]
        # kill 1 biggest elements + 2 smallest elements = A[n-2] - A[2]
        # kill 2 biggest elements + 1 smallest elements = A[n-3] - A[1]
        # kill 3 biggest elements = A[n-4] - A[0]