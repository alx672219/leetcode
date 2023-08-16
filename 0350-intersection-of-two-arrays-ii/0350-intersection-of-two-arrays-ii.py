from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): 
            return self.intersect(nums2, nums1) # 길이가 짧은게 기준
        
        cnt = Counter(nums1) # ex) Counter({4: 1, 9: 1, 5: 1})
        ans = []
        for x in nums2:      # x = 9
            if cnt[x] > 0:   # cnt[x] = 1 which is # of 9 in shorter list
                ans.append(x)
                cnt[x] -= 1  # ex) Counter({4: 1, 5: 1, 9: 0})
        return ans