class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result = ""
        word = ""

        for i in range(len(title) + 1):
            if i == len(title) or title[i] == ' ':
                n = len(word)

                for j in range(n):
                    ch = word[j]
                    ascii_val = ord(ch)

                    if n <= 2:
                        if 65 <= ascii_val <= 90:
                            ch = chr(ascii_val + 32)
                    else:
                        if j == 0:
                            if 97 <= ascii_val <= 122:
                                ch = chr(ascii_val - 32)
                        else:
                            if 65 <= ascii_val <= 90:
                                ch = chr(ascii_val + 32)

                    result += ch

                if i < len(title):
                    result += ' '

                word = ""
            else:
                word += title[i]

        return result
