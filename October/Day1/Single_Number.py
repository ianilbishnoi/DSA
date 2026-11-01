#bruteforce
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            count = 0

            for j in nums:
                if i == j:
                    count += 1

            if count == 1:
                return i



#optimal--> XOR
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for i in nums:
            result = result ^ i

        return result
