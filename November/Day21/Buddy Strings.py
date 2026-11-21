class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        first = -1
        second = -1
        for i in range(len(s)):
            if s[i] != goal[i]:
                if first == -1:
                    first = i
                elif second == -1:
                    second = i
                else:
                    return False
        if first == -1:
            freq = [0] * 26
            for ch in s:
                index = ord(ch) - ord('a')
                freq[index] += 1
                if freq[index] > 1:
                    return True
            return False
        if second == -1:
            return False
        return s[first] == goal[second] and s[second] == goal[first]
