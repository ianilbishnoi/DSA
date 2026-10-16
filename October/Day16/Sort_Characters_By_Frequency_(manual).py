class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        chars = list(freq)

        for i in range(1, len(chars)):
            key = chars[i]
            j = i - 1

            while j >= 0 and freq[chars[j]] < freq[key]:
                chars[j + 1] = chars[j]
                j -= 1

            chars[j + 1] = key

        result = ""

        for ch in chars:
            result += ch * freq[ch]

        return result


#other method by using sorted()

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        chars = sorted(freq, key=lambda ch: freq[ch], reverse=True)

        result = ""

        for ch in chars:
            result += ch * freq[ch]

        return result
