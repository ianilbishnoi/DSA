class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            for j in range(n - i - 1):
                if nums[j] % 2 == 1 and nums[j + 1] % 2 == 0:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums

#sort array by parity --> even numbers, odd numbers --> unsorted[3,1,2,4] --> sorted --> [2,4,1,3] / [2,4,3,1] / [4,2,1,3] / [4,2,3,1]
