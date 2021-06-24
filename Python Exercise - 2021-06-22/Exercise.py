import os
import re
import sys
import logging
import getopt
from typing import Counter

class Logging(object):
    def __init__(self):
        self.__log_dir = os.path.join(os.getcwd(),"fileparser.log")
    def WriteLog(self,contents):
        logging.basicConfig(filename=self.__log_dir,filemode='a+',format='%(asctime)s - %(message)s', level=logging.DEBUG)
        logging.debug(contents)
    

class FileParser(object):
    def __init__(self) -> None:
        self.__input_dir = None
        self.__output_dir = None
        self.__config_dir = os.path.join(os.getcwd(),'config')
        self.__log = Logging()
        self.__list = list()
        self.__get_io_file()
        
    
    def __get_config(self):
        return self.__config_dir

    
    def __get_io_file(self):
        try:
            with open(self.__config_dir,"r") as f:
                lines = f.readlines()
                if len(lines) != 0:
                    self.__input_dir = lines[0].replace('\n','').split('=')[1]
                    self.__output_dir = lines[1].split('=')[1]
            self.__log.WriteLog(f"{self.__config_dir} file opened and directories are read.")
        except FileNotFoundError as e:
            print("Exception : ",e)
    
    def Open(self)->list:
        try:
            with open(self.__input_dir,"r") as f:
                for i in f.read().lower().replace('\n','; ').split(' '):
                    self.__list.append(str(i))
            self.__log.WriteLog(f"{self.__input_dir} file opened and read all the contents into a list.")
            return self.__list
        except FileNotFoundError as e:
            print("Exception : ",e)
        
    def Write(self,contents,opener):
        try:
            with open(self.__output_dir,opener) as f:
                f.write(contents)
            self.__log.WriteLog(f"{self.__output_dir} file opened and contents written.")
        except FileNotFoundError as e:
            print("Exception : ",e)
        

class WriteConfig(FileParser):
    def __init__(self) -> None:
        super().__init__()
        self.__config = super()._FileParser__get_config()
        self.__log = Logging()

    def write(self):
        try:
            opts, _ = getopt.getopt(sys.argv[1:],"i:o:",["input=","output="])
            with open(self.__config,"w+") as f:
                for i,j in opts:
                    if i == '-i':
                        f.write(f"Input_file={j}\n")
                    elif i == '-o':
                        f.write(f"Output_file={j}")
            self.__log.WriteLog(f"{self.__config} file opened and directories are set.")
        except getopt.GetoptError as e:
            print("GetOptError Exception : ",e)
            sys.exit()
        except FileNotFoundError as e:
            print("FileNotFoundError Exception : ",e)
                
    
class Operations(FileParser):
    def __init__(self) -> None:
        super().__init__()
        self.__list = super().Open()
        self.__countTo = int()
        self.__countIng = int()
        self.__counter = Counter(self.__list)
        self.__log = Logging()

    def printall(self):
        self.findTO()
        self.findING()
        self.find_max_words()
        self.palindrome()
        self.find_unique_list()
        self.word_dict()
        self.splitvowels()
        self.capatilize_3_letter()
        self.capatilize_5_Word()
        self.change_blankspace()
        self.split_using_semicolon()
        self.__log.WriteLog(f"Operations are done")

    def findTO(self):
        try:
            assert len(self.__list) > 1
            for i in self.__list:
                if i.startswith("to"):
                    self.__countTo += 1
            print(f"The number of words having prefix with \"To\" in the input file = {self.__countTo}")
        except AssertionError:
            print('Passed an empty file')

    def findING(self):
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
        self.__dict = {i:self.__list.index(i) for i in self.__list }
        print(f"word dict {self.__dict}")

    def __write_output(self,type,opener):
        if type == "vowels":
            contents = ''
            for i in self.__list:
                contents += " ".join(re.split('a|e|i|o|u',i))+","
            super().Write(contents,opener)
        if type == "capitalize3":
            super().Write('\n',opener)
            for i in self.__list:
                if i != ';':
                    temp = i[2].upper()
                    super().Write(i[:2]+temp+i[3:]+" ",opener)
        if type == "capitalize5":
            super().Write('\n',opener)
            for i,j in enumerate(self.__list):
                if j != ';' and i == 5:
                    super().Write(j.upper()+" ",opener)
                elif i != 5 and j != ';':
                    super().Write(j+" ",opener)
        if type == "-space":
            super().Write('\n',opener)
            for j,i in enumerate(self.__list):
                if i != ';' and j != len(self.__list)-1:
                    super().Write(i+'-',opener)
                elif j == len(self.__list)-1:
                    super().Write(i,opener)
        if type == "semicolon":                    
            super().Write('\n',opener)
            for i in self.__list:
                super().Write(i,opener)
        
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

w = WriteConfig()
assert isinstance(w,WriteConfig)
w.write()

o = Operations()
assert isinstance(o,Operations)
o.printall()


