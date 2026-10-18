class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        size = 1

        while size < n:
            result = nums[:]
            start = 0

            while start < n:
                mid = min(start + size, n)
                end = min(start + 2 * size, n)

                i, j, k = start, mid, start

                while i < mid and j < end:
                    if nums[i] <= nums[j]:
                        result[k] = nums[i]
                        i += 1
                    else:
                        result[k] = nums[j]
                        j += 1
                    k += 1

                while i < mid:
                    result[k] = nums[i]
                    i += 1
                    k += 1

                while j < end:
                    result[k] = nums[j]
                    j += 1
                    k += 1

                start += 2 * size

            nums = result
            size *= 2

        return nums
