class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1
        result = ""
        while len(freq) > 0:
            max_char = ""
            max_freq = 0
            for ch in freq:
                if freq[ch] > max_freq:
                    max_freq = freq[ch]
                    max_char = ch
            result += max_char * max_freq
            del freq[max_char]
        return result
