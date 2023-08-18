class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            x = ord(char) - ord('A') + 1   # ord('B') is ascii of b
                                        # ord(char) - ord('A') + 1 is getting number 
                                        # A = 1, B = 2, ... Z = 26 
            result = result * 26 + x
        return result