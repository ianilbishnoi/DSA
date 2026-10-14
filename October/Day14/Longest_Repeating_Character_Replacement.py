
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            # Count the current character
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1

            # Track the most frequent character
            max_freq = max(max_freq, count[s[right]])

            # Shrink the window if too many replacements are needed
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # Update the longest valid substring
            max_len = max(max_len, right - left + 1)

        return max_len


