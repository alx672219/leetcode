class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums))[::-1]: # 뒤에서 부터 iterate 안하면 append 할때 자동으로 숫자들이 앞으로 한칸씩 이동한다.
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)