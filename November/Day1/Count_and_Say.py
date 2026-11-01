class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for i in range(n - 1):
            s = ""
            j = 0

            while j < len(result):
                count = 1

                while j + 1 < len(result) and result[j] == result[j + 1]:
                    count += 1
                    j += 1

                s += str(count) + result[j]
                j += 1

            result = s

        return result
