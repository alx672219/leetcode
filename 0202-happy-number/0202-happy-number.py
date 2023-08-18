class Solution:
    def isHappy(self, n: int) -> bool:
        dictionary = set()
        while not n in dictionary: # dictionary에 넣은 이유는 cycle 때문에
            dictionary.add(n)
            string = str(n)
            c = 0
            for i in string:
                c += int(i) ** 2
            n = c

            if n == 1:
                return True
        return False