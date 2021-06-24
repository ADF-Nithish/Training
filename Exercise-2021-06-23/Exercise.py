"""
This python file is an Example of how to write a clean code.
"""
import os
import re
import sys
import logging
import getopt
from typing import Counter


class Logging:
    """
    This class is used to write all the Logs to a file.
    Attributes
        log_dir : str (path for the log directory file).
    Methods
        write_log(contents) : logging (writes the log to the logfile).
    """
    def __init__(self):
        self.__log_dir = os.path.join(os.getcwd(),"fileparser.log")
    def finish(self):
        """
        Logging Finished
        """
        file = self.__log_dir.split('\\')[-1]
        logging.info(" %s %s",'Finished Logging',file)
    def write_log(self,contents):
        """
        This method is used to write the content to a file.
        """
        logging.basicConfig(
            filename=self.__log_dir,
            filemode='a+',
            format='%(asctime)s - %(message)s',
            level=logging.DEBUG
        )
        logging.debug('%s',contents)
        self.finish()

class FileParser:
    """
    FileParser used to read and write file.
    """
    def __init__(self) -> None:
        self.__input_dir = None
        self.__output_dir = None
        self.__config_dir = os.path.join(os.getcwd(),'.config')
        self.__log = Logging()
        self.__list = list()
        self.__get_io_file()

    def get_config(self):
        """
        returns config directory.
        """
        return self.__config_dir

    def __get_io_file(self):
        """
        returns list of words.
        """
        try:
            with open(self.__config_dir,"r") as file:
                lines = file.readlines()
                if len(lines) != 0:
                    self.__input_dir = lines[0].replace('\n','').split('=')[1]
                    self.__output_dir = lines[1].split('=')[1]
            self.__log.write_log("config file opened and directories are read.")
        except FileNotFoundError as ex:
            print("Exception : ",ex)

    def open(self):
        """
        opens a file to read.
        """
        log_detail = "file opened and read all the contents into a list."
        try:
            with open(self.__input_dir,"r") as file:
                for i in file.read().lower().replace('\n','; ').split(' '):
                    self.__list.append(str(i))
            self.__log.write_log(f"input {log_detail}")
            return self.__list
        except FileNotFoundError as ex:
            print("Exception : ",ex)
            return self.__list

    def write(self,contents,opener):
        """
        writes a file.
        """
        try:
            with open(self.__output_dir,opener) as file:
                file.write(contents)
            self.__log.write_log("output file opened and contents written.")
        except FileNotFoundError as ex:
            print("Exception : ",ex)


class WriteConfig(FileParser):
    """
    Config file operations are done using this class
    """
    def __init__(self) -> None:
        super().__init__()
        self.__config = super().get_config()
        self.__log = Logging()

    def write_config(self):
        """
        writes into config file.
        """
        try:
            opts, _ = getopt.getopt(sys.argv[1:],"i:o:",["input=","output="])
            with open(self.__config,"w+") as file:
                for i,j in opts:
                    if i == '-i':
                        file.write(f"Input_file={j}\n")
                    elif i == '-o':
                        file.write(f"Output_file={j}")
            self.__log.write_log("config file opened and directories are set.")
        except getopt.GetoptError as ex:
            print("GetOptError Exception : ",ex)
            sys.exit()
        except FileNotFoundError as ex:
            print("FileNotFoundError Exception : ",ex)

class Operations(FileParser):
    """
    This class is used to do all operations on the list of string.
    """
    def __init__(self) -> None:
        super().__init__()
        self.__list = super().open()
        self.__count_to = int()
        self.__count_ing = int()
        self.__counter = Counter(self.__list)
        self.__log = Logging()

    def printall(self):
        """
        prints all methods of operation class.
        """
        self.find_to()
        self.find_ing()
        self.find_max_words()
        self.palindrome()
        self.find_unique_list()
        self.word_dict()
        self.splitvowels()
        self.capatilize_3_letter()
        self.capatilize_5_word()
        self.change_blankspace()
        self.split_using_semicolon()
        self.__log.write_log("Operations are done")

    def find_to(self):
        """
        return a string starting with To.
        """
        log_detail = "The number of words having prefix with \"To\" in the input file ="
        try:
            assert len(self.__list) > 1
            for i in self.__list:
                if i.startswith("to"):
                    self.__count_to += 1
            print(f"{log_detail} {self.__count_to}")
        except AssertionError:
            print('Passed an empty file')

    def find_ing(self):
        """
        return a string starting with Ing.
        """
        try:
            assert len(self.__list) > 1
            for i in self.__list:
                if i.endswith("ing"):
                    self.__count_ing +=1
            print(f"The number of words ending with \"ing\" in the input file = {self.__count_ing}")
        except AssertionError:
            print("Passed an empty file")
    def find_max_words(self):
        """
        return max number of words.
        """
        log_detail = "The word that was repeated maximum number of times is"
        try:
            assert self.__counter.most_common(1)[0][1] > 1
            print(f"{log_detail} {self.__counter.most_common(1)[0][0]}")
        except AssertionError:
            print("All words are repeated exactly once, So maximum cannot be found")

    def palindrome(self):
        """
        returns a palindrome.
        """
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
        """
        returns all the unique elements from the list.
        """
        unique_list = [i for i in self.__list if self.__list.count(i) == 1]
        try:
            assert len(unique_list) > 0
            print(f"Unique elements in a list are: {unique_list}")
        except AssertionError:
            print("No unique elements in the file")
    def word_dict(self):
        """
        return the dictionary with key as the word and values as index.
        """
        dictt = {i:self.__list.index(i) for i in self.__list }
        print(f"word dict {dictt}")

    def splitvowels(self):
        """
        calls the private write ouput function with specific type(vowels).
        """
        contents = ''
        for i in self.__list:
            contents += " ".join(re.split('a|e|i|o|u',i))+","
        super().write(contents,'w+')
    def capatilize_3_letter(self):
        """
        calls the private write ouput function with specific type(vowels).
        """
        super().write('\n','a+')
        for i in self.__list:
            if i != ';':
                temp = i[2].upper()
                super().write(i[:2]+temp+i[3:]+" ",'a+')
    def capatilize_5_word(self):
        """
        calls the private write ouput function with specific type(vowels).
        """
        super().write('\n','a+')
        for i,j in enumerate(self.__list):
            if j != ';' and i == 5:
                super().write(j.upper()+" ",'a+')
            elif i != 5 and j != ';':
                super().write(j+" ",'a+')
    def change_blankspace(self):
        """
        calls the private write ouput function with specific type(vowels).
        """
        super().write('\n','a+')
        for j,i in enumerate(self.__list):
            if i != ';' and j != len(self.__list)-1:
                super().write(i+'-','a+')
            elif j == len(self.__list)-1:
                super().write(i,'a+')
    def split_using_semicolon(self):
        """
        calls the private write ouput function with specific type(vowels).
        """
        super().write('\n','a+')
        for i in self.__list:
            super().write(i,'a+')

w = WriteConfig()
assert isinstance(w,WriteConfig)
w.write_config()

o = Operations()
assert isinstance(o,Operations)
o.printall()
