class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        word = ""

        for ch in s:
            if ch != " ":
                word = ch + word
            else:
                result += word + " "
                word = ""

        result += word

        return result
