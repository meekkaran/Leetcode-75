class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.convert(num1) * self.convert(num2))
    #create a function that converts a string to int using ascii
    def convert(self,s):
        result = 0
        for i in range(len(s)):
            result = result * 10 + ord(s[i])- ord('0')
        return result
