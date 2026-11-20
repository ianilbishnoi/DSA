class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        for length in range(n, 0, -1):
            for i in range(n - length + 1):
                sub = s[i:i + length]
                nice = True
                for ch in sub:
                    if ord(ch) >= 97:
                        other = chr(ord(ch) - 32)
                    else:
                        other = chr(ord(ch) + 32)
                    if other not in sub:
                        nice = False
                        break
                if nice:
                    return sub
        return ""
