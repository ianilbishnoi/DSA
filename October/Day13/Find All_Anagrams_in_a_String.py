#using python slicing
#bruteforce
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        result = []
        m = len(p)
        for i in range(len(s) - m + 1):
            if sorted(s[i:i + m]) == sorted(p):
                result.append(i)
        return result

  #s[i:i+m] = extracts a substring starting at index i and ending just before index i + m
  #sorted --> sort the string




#optimized by converting characters into ASCII values
#ord(s[i]) --> character in string s at index i converts into its ascii value ,, a - 97, b-98, z-122 

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n, m = len(s), len(p)
        if m > n:
            return []

        result = []
        a = [0] * 26
        b = [0] * 26

        for i in range(m):
            a[ord(s[i]) - 97] += 1
            b[ord(p[i]) - 97] += 1

        for i in range(n - m + 1):
            if a == b:
                result.append(i)

            if i + m < n:
                a[ord(s[i]) - 97] -= 1
                a[ord(s[i + m]) - 97] += 1

        return result
