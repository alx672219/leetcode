class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):  # n의 개수 만큼 
            nums1[i + m] = nums2[i]
            # m 다음에 merge 한다
        
        nums1.sort()