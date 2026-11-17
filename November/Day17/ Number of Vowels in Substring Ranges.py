class Solution:
    def vowelStrings(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i]

            if s[i] in "aeiou":
                prefix[i + 1] += 1

        ans = []

        for l, r in queries:
            ans.append(prefix[r + 1] - prefix[l])

        return ans