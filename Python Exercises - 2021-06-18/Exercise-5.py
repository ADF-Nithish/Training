"""
Program to Convert Decimal to Binary, Octal and Hexadecimal
"""
import sys

class Solution(object):
    def __init__(self,decimal):
        self.__decimal = decimal
    def toBinary(self):
        return f"Binary of {self.__decimal} - "+bin(self.__decimal)[2:]
    def toOctal(self):
        return f"Octal of {self.__decimal} - "+oct(self.__decimal)[2:]
    def toHexadecimal(self):
        return f"HexaDecimal of {self.__decimal} - "+hex(self.__decimal)[2:]


decimal = sys.argv[1]

s = Solution(decimal=decimal)
print(s.toBinary())
print(s.toOctal())
print(s.toHexadecimal())