#bruteforce
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        for capacity in range(max(weights), sum(weights) + 1):
            days_needed = 1
            current = 0

            for weight in weights:
                if current + weight > capacity:
                    days_needed += 1
                    current = 0

                current += weight

            if days_needed <= days:
                return capacity



#optimal
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)  # minimum possible capacity
        right = sum(weights)  # maximum possible capacity

        while left < right:
            mid = (left + right) // 2
            days_needed = 1
            current = 0

            for weight in weights:
                if current + weight > mid:
                    days_needed += 1
                    current = 0

                current += weight

            if days_needed <= days:
                right = mid  # try a smaller capacity
            else:
                left = mid + 1  # increase capacity

        return left
