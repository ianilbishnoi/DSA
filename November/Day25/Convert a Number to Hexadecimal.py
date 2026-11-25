class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        digits = "0123456789abcdef"
        num = num & 0xffffffff       
        result = ""
        while num > 0:
            rem = num % 16
            result = digits[rem] + result
            num = num // 16
        return result
