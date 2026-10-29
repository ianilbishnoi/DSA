class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)

        for i in range(n):
            for j in range(i + 1, n):
                if intervals[i][0] > intervals[j][0]:
                    intervals[i], intervals[j] = intervals[j], intervals[i]

        result = [intervals[0]]

        for i in range(1, n):
            if intervals[i][0] <= result[-1][1]:
                if intervals[i][1] > result[-1][1]:
                    result[-1][1] = intervals[i][1]
            else:
                result = result + [intervals[i]]

        return result
