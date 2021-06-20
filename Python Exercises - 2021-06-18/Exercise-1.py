"""
Program to read a file and store the unique words in a 
list sorted based on the length of word in a new file 
along with each word length appended to it.

"""

import os
import sys


class Solution(object):
    
    def __init__(self):
        self.__list = None

    def open(self,dir:str):
        try:
            with open(dir,"r") as f:
                self.__list = [i for i in str(f.read()).strip().lower().split()]
            self.__list.sort(key=lambda x:len(x))
        except FileNotFoundError as e:
            self.__list = "Exception "+ e

    def __repr__(self) -> str:
        return str(self.__list)

    def unique(self):
        temp_dict = {i:self.__list.count(i) for i in self.__list}
        self.__list  = [i for i,j in temp_dict.items() if j == 1]

    def write(self,dir:str):
        with open(dir,'w+') as f:
            for i in self.__list:
                f.write(i+' '+str(len(i))+'\n')


if __name__ == "__main__":
    filename = sys.argv[1]
    ans_filename = sys.argv[2]

    dir = os.path.join(os.getcwd(),filename)
    ans = os.path.join(os.getcwd(),ans_filename)

    s = Solution()
    s.open(filename)
    s.unique()
    s.write(ans)
    print(s)


"""
Command Line Argument:

py Exercise-1.py <Input File> <Output File>

eg:
    py Exercise-1.py Exercise-1.txt Exercise-1-ans.txt
"""

