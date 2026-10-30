class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        speed = 1

        while speed <= max(piles):
            hours = 0

            for pile in piles:
                hours += (pile + speed - 1) // speed

            if hours <= h:
                return speed

            speed += 1

        return speed
