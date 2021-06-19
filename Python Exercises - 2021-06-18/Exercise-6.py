"""
Program to Find ASCII Value of Character.
"""

class Solution(object):
    def __init__(self,char) -> None:
        self.__char = char
    def find_ASCII(self):
        return ord(self.__char)
    
s = Solution('a')
print(s.find_ASCII())

#Command Line Podanum