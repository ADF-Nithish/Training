"""
Program to read a CSV (CSV with n number of columns) and store it in DICT of list.
"""

import os
import sys

class Solution(object):
    def __init__(self):
        self.__dict = None
    
    def open(self,dir:str):
        try:
            with open(dir,'r') as f:
                columns = str(f.readline()).strip().split(',')
                self.__dict = {i:[] for i in columns}
                for line in f.readlines():
                    for i,j in enumerate(line.strip().split(',')):
                        self.__dict[columns[i]].append(j)
        except Exception as e:
            print(e)
            
    def get_dict_list(self):
        return self.__dict

if __name__ == "__main__":
    filename = sys.argv[1]
    dir = os.path.join(os.getcwd(),filename)

    s = Solution()
    s.open(dir)
    print(s.get_dict_list())


"""
Command Line Arguments:
py Exercise.py <Input File> <Output File>

eg:
py Exercise-2.py Exercise-2.csv
"""
    