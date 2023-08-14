class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers (i, j)
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum(): # remove non-alphanumeric characters and space
                i += 1 # remove 한 후에 alphanumeric 찾으러 이동
            while i < j and not s[j].isalnum(): # remove non-alphanumeric characters and space
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1 # 하나씩 줄여나간다
            j -= 1

        return True