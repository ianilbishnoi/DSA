class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        first = -1
        second = -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if first == -1:
                    first = i
                elif second == -1:
                    second = i
                else:
                    return False
        if first == -1:
            return True
        if second == -1:
            return False
        if s1[first] == s2[second] and s1[second] == s2[first]:
            return True
        return False
