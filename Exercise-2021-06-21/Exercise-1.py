from io import TextIOWrapper
import os
import sys
from collections import Counter
import re


class Parser(object):
    def __init__(self,in_dir:str,out_dir:str) -> None:
        self.__input_dir = in_dir
        self.__output_dir = out_dir
        self.__f = TextIOWrapper
        self.__countTo = int()
        self.__countIng = int()
        self.__list = list()
        self.__unique_list = list()
        self.__dict = dict()

        self.__list_of_words_in_a_file()
        
        self.__counter = Counter(self.__list)
    
    def __list_of_words_in_a_file(self):
        with open(self.__input_dir,"r") as self.__f:
            for i in self.__f.read().lower().replace('\n','; ').split(' '):
                self.__list.append(str(i))
    
    def find_TO(self):
        try:
            assert len(self.__list) > 1
            for i in self.__list:
                if i.startswith("to"):
                    self.__countTo += 1
            print(f"The number of words having prefix with \"To\" in the input file = {self.__countTo}")
        except AssertionError:
            print('Passed an empty file')
    
    def find_ING(self):
        try:
            assert len(self.__list) > 1
            for i in self.__list:
                if i.endswith("ing"):
                    self.__countIng +=1
            print(f"The number of words ending with \"ing\" in the input file = {self.__countIng}")
        except AssertionError:
            print("Passed an empty file")
    
    def find_max_words(self):
        try:
            assert self.__counter.most_common(1)[0][1] > 1
            print(f"The word that was repeated maximum number of times is {self.__counter.most_common(1)[0][0]}")
        except AssertionError:
            print("All words are repeated exactly once, So maximum cannot be found")
    
    def palindrome(self):
        try:
            assert len(self.__list) > 1 
            flag = 0
            print("The palindrome present in the files are: ",end=' ')
            for i in self.__list:
                if i == i[::-1]:
                    print(i)
                else:
                    flag += 1
            if flag == len(self.__list):
                print("Null")
        except AssertionError:
            print("Passed an empty file")

    def find_unique_list(self):
        self.__unique_list = [i for i in self.__list if self.__list.count(i) == 1]
        try:
            assert len(self.__unique_list) > 0
            print(f"Unique elements in a list are: {self.__unique_list}",)            
        except AssertionError:
            print("No unique elements in the file")
    
    def word_dict(self):
        self.__dict = {self.__list[i]:self.__list.index(i) for i in self.__list }
        print(f"word dict {self.__dict}")

    def __write_output(self,open_type,r):
        try:
            with open(self.__output_dir,r) as self.__f:
                if open_type == "vowels":
                    for i in self.__list:
                        self.__f.write(" ".join(re.split('a|e|i|o|u',i))+",")
                if open_type == "capitalize3":
                    self.__f.write('\n')
                    for i in self.__list:
                        if i != ';':
                            temp = i[2].upper()
                            self.__f.write(i[:2]+temp+i[3:]+" ")
                if open_type == "capitalize5":
                    self.__f.write('\n')
                    for i,j in enumerate(self.__list):
                        if j != ';' and i == 5:
                            self.__f.write(j.upper()+" ")
                        elif i != 5 and j != ';':
                            self.__f.write(j+" ")
                if open_type == "-space":
                    self.__f.write('\n')
                    for j,i in enumerate(self.__list):
                        if i != ';' and j != len(self.__list)-1:
                            self.__f.write(i+'-')
                        elif j == len(self.__list)-1:
                            self.__f.write(i)
                if open_type == "semicolon":                    
                    self.__f.write('\n')
                    for i in self.__list:
                        self.__f.write(i)
                
        except FileNotFoundError as e:
            print("Exception: ",e)
        
    def splitvowels(self):
        return self.__write_output("vowels","w+")
    def capatilize_3_letter(self):
        return self.__write_output("capitalize3","a+")
    def capatilize_5_Word(self):
        return self.__write_output("capitalize5","a+")
    def change_blankspace(self):
        return self.__write_output("-space","a+")
    def split_using_semicolon(self):
        return self.__write_output("semicolon","a+")
        
        
    
if __name__ == "__main__":
    try:
        in_dir = os.path.join(os.getcwd(),sys.argv[1])
    except FileNotFoundError as e:
        print("Exception: ",e)

    out_dir = os.path.join(os.getcwd(),sys.argv[2])

    p = Parser(in_dir,out_dir)
    assert isinstance(p,Parser),"object not valid"
    p.find_TO()
    p.find_ING()
    p.find_max_words()
    p.palindrome()
    p.find_unique_list()
    p.word_dict()
    p.splitvowels()
    p.capatilize_3_letter()
    p.capatilize_5_Word()
    p.change_blankspace()
    p.split_using_semicolon()