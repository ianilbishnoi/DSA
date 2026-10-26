class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1



#guess(mid) --> built in api guess(num)
#guess(num) == 0: guessed correctly
#guess(num) == -1: guess is too high
#guess(num) == 1: guess is too low
