#Sliding Window + Frequency
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        freq = {}
        for ch in t:
            if ch not in freq:
                freq[ch] = 0
            freq[ch] += 1
        left = 0
        required = len(t)
        start = 0
        min_len = len(s) + 1
        for right in range(len(s)):
            ch = s[right]
            if ch in freq:
                if freq[ch] > 0:
                    required -= 1
                freq[ch] -= 1
            while required == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left
                ch = s[left]
                if ch in freq:
                    freq[ch] += 1

                    if freq[ch] > 0:
                        required += 1
                left += 1
        if min_len == len(s) + 1:
            return ""
        return s[start:start + min_len]
