#using python slicing
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)

        for i in range(len(s2) - m + 1):
            if sorted(s2[i:i + m]) == sorted(s1):
                return True

        return False

  #not optimal
