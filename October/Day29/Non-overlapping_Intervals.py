class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)

        for i in range(n - 1):
            min_idx = i

            for j in range(i + 1, n):
                if intervals[j][1] < intervals[min_idx][1]:
                    min_idx = j

            intervals[i], intervals[min_idx] = intervals[min_idx], intervals[i]

        count = 0
        end = intervals[0][1]

        for i in range(1, n):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]

        return count
