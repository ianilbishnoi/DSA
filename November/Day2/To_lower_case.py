#using .lower()
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()


#using ord(i) --> returns the ASCII value of a character, A - 65, B - 66..., a - 97, b - 98
class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""

        for i in s:
            if 'A' <= i <= 'Z':
                result += chr(ord(i) + 32) #The difference is 32, so add 32 to convert uppercase to lowercase
            else:
                result += i

        return result

#Uppercase letters A-Z have ASCII values 65-90
#Lowercase letters a-z have ASCII values 97-122
#The difference is 32, so add 32 to convert uppercase to lowercase.
#chr() converts the ASCII value back into a character
