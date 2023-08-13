class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 1 and digits[0] == 9: # 한자리수 이고 9일때 
            return [1,0]

        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1]) # 마지막 자리만 빼고 다
            return digits