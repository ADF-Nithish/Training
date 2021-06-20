"""
Program to Find ASCII Value of Character.
"""
import sys

class Solution(object):
    def __init__(self,char) -> None:
        self.__char = char
    def find_ASCII(self):
        return ord(self.__char)

if __name__ == "__main__":   
    char = sys.argv[1]
    s = Solution(char=char)
    print(s.find_ASCII())

"""
Command Line Arguement:
    py Exercise-6.py <input>
eg:
    py Exercise-6.py a
"""