class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])   # sort the intervals by the first value in each interval
        output = [intervals[0]]

        for start, end in intervals[1:]:
            prev_end = output[-1][1]

            if prev_end >= start:
                output[-1][1] = max(prev_end, end)
            else:
                output.append([start, end])
        return output