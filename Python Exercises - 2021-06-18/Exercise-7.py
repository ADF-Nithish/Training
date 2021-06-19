"""
Program to get an application (name , age , gender, salary, state, city)
"""

class Application(object):
    def __init__(self,name) -> None:
        self.__name = name

app = Application('Nithish')
