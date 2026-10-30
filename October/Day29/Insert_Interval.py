class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            result += [intervals[i]]
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            if intervals[i][0] < newInterval[0]:
                newInterval[0] = intervals[i][0]

            if intervals[i][1] > newInterval[1]:
                newInterval[1] = intervals[i][1]

            i += 1

        result += [newInterval]

        while i < n:
            result += [intervals[i]]
            i += 1

        return result
