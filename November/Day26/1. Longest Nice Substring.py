class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                nice = True

                for ch in sub:
                    if ch.islower():
                        if ch.upper() not in sub:
                            nice = False
                            break

                    elif ch.isupper():
                        if ch.lower() not in sub:
                            nice = False
                            break

                if nice and len(sub) > len(longest):
                    longest = sub

        return longest
