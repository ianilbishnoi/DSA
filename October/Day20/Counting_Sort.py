class Solution:
    def countingSort(self, arr):
        maximum = max(arr)
        count = [0] * (maximum + 1)

        for num in arr:
            count[num] += 1

        result = []
        for i in range(len(count)):
            while count[i] > 0:
                result += [i]
                count[i] -= 1

        return result
