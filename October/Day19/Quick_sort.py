class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(low, high):
            if low >= high:
                return

            pivot = nums[high]
            i = low

            for j in range(low, high):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[high] = nums[high], nums[i]

            quicksort(low, i - 1)
            quicksort(i + 1, high)

        quicksort(0, len(nums) - 1)
        return nums
