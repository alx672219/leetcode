class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {}
        for i in range(len(keyboard)):
            d[keyboard[i]] = i
        total = 0
        current = 0
        for c in word:
            total += abs(d[c]-current) # 현재 손가락에서 원하는 키보드까지의 거리
            current = d[c] # 현재 손가락의 위치
        return total