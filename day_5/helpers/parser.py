"""
[Parser used to pass command line arguments]
"""
import argparse

class Parser:
    def __init__(self,prog:str,description:str):
        self.parser = argparse.ArgumentParser(
            prog=prog,
            description = description,
            )
    def add_argument(self,name:str,metavar:str,specific_help:str):
        """
        [add arguments to parser]
        """
        self.parser.add_argument(
            name,
            metavar=metavar,
            help=specific_help)
    def get_args(self):
        """
        Returns:
            [args]: [all the args passed]
        """
        return self.parser.parse_args()