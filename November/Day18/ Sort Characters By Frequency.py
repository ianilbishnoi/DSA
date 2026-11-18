class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        result = ""

        for ch in sorted(freq, key=lambda x: freq[x], reverse=True):
            result += ch * freq[ch]

        return result