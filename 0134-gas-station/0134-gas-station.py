class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): # 만약에 한바퀴를 다 돌 수 있다면 아무 index에서 시작가능
            return -1

        total = 0
        starting_index = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i]) # gain[i] = gas[i] - cost[i] 이 문제의 공식

            if total < 0:
                total = 0
                starting_index = i + 1

        return starting_index
