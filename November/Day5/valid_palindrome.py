class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            a = ord(s[left])
            b = ord(s[right])

            # skip non-alphanumeric characters
            if not (48 <= a <= 57 or 65 <= a <= 90 or 97 <= a <= 122):
                left += 1
                continue

            if not (48 <= b <= 57 or 65 <= b <= 90 or 97 <= b <= 122):
                right -= 1
                continue

            # convert uppercase to lowercase
            if 65 <= a <= 90:
                a += 32

            if 65 <= b <= 90:
                b += 32

            if a != b:
                return False

            left += 1
            right -= 1

        return True
