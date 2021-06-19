"""
Program to get an application (name , age , gender, salary, state, city)
"""
import sys

class Application(object):
    def __init__(self,*iterables) -> None:
        self.__name = iterables[0]
        self.__age = iterables[1]
        self.__gender = iterables[2]
        self.__salary = iterables[3]
        self.__state = iterables[4]
        self.__city = iterables[5]
    
    def __getvalue(self):
        return " , ".join(["Name: "+str(self.__name),"Age: "+str(self.__age), "Gender: "+str(self.__gender), "Salary: "+str(self.__salary), "State: "+str(self.__state), "City: "+str(self.__city)])
    def __repr__(self) -> str:
        return self.__class__.__name__+"("+self.__getvalue()+")"
    

app = Application(*sys.argv[1:])
print(app)

"""
Command Line Arguement:
    py Exercise-7.py <inputs>
Eg:
    py Exercise-7.py Nithish 20 Male 18000 Tamilnadu Coimbatore
"""