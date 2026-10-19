class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(low, high):
            if low >= high:
                return

            pivot = nums[high]
            i = low
            j = low
            k = high

            while j <= k:
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                elif nums[j] > pivot:
                    nums[j], nums[k] = nums[k], nums[j]
                    k -= 1
                else:
                    j += 1

            quicksort(low, i - 1)
            quicksort(k + 1, high)

        quicksort(0, len(nums) - 1)
        return nums
