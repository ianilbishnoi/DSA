
#brute force method
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and abs(i-j) <= k:
                    return True
                
        return False

#time complexity O(n^2) --> worst case


#Optimized code with Hashmap


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen and i - seen[nums[i]] <= k:
                return True
            seen[nums[i]] = i
        return False

#time complexity O(n)
#i - seen[nums[i]] --> distance between indices
#example nums = [1, 2, 3, 1] ; k = 3
#i - seen[nums[i]] = 3 - seen[1] = 3 - 0 = 3


  
