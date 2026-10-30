class Solution:
    def findPages(self, arr, k):
        if k > len(arr):
            return -1

        left = max(arr)
        right = sum(arr)

        while left <= right:
            mid = (left + right) // 2
            students = 1
            pages = 0

            for book in arr:
                if pages + book <= mid:
                    pages += book
                else:
                    students += 1
                    pages = book

            if students > k:
                left = mid + 1
            else:
                right = mid - 1

        return left
