"""
Program to Find HCF or GCD
"""
import sys

class Solution(object):
    def __init__(self,*iterables) -> None:
        self.__list = iterables
        self.gcd = self.__gcd()
        
    def __gcd(self) -> int:
        gcd = self.__list[0]
        for i in range(1,len(self.__list)):
            gcd = self.__gcd_helper(gcd,self.__list[i])
        return gcd

    def __gcd_helper(self,first:int,second:int) -> int:
        while second:
            first, second = second, first % second
        return first

iterables = map(int,sys.argv[1:])

s = Solution(*iterables)
print(s.gcd)

"""
Command Line Arguement:
    py Exercise-4.py <input>
eg:
    py Exercise-4.py 4 8 16 32
"""

