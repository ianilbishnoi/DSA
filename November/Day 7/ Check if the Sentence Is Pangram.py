class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = [False] * 26
        for ch in sentence:
            index = ord(ch) - ord('a')
            seen[index] = True
        for i in range(26):
            if seen[i] == False:
                return False
        return True
