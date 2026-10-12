class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        total = 0
        min_length = len(nums) + 1

        for right in range(len(nums)):
            # Add the current element to the sum
            total += nums[right]

            # If the sum reaches the target, try to make the subarray smaller
            while total >= target:
                length = right - left + 1

                # Update the minimum length if we find a shorter subarray
                min_length = min(min_length, length)

                # Remove the leftmost element and move left forward
                total -= nums[left]
                left += 1

        # Return 0 if no subarray reaches the target
        if min_length == len(nums) + 1:
            return 0

        return min_length
