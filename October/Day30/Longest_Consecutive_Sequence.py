class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for num in nums:
            current = num
            count = 1

            while True:
                found = False

                for x in nums:
                    if x == current + 1:
                        found = True
                        break

                if found:
                    current += 1
                    count += 1
                else:
                    break

            if count > longest:
                longest = count

        return longest
