class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        low = 0
        high = len(nums) - 1

        while low <= high:
            pivot = nums[high]
            i = low

            for j in range(low, high):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1

            nums[i], nums[high] = nums[high], nums[i]

            if i == target:
                return nums[i]
            elif i < target:
                low = i + 1
            else:
                high = i - 1
