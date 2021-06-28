"""
[Parser used to pass command line arguments]
"""
import argparse
import datetime

class Parser:
    def __init__(self,prog:str,description:str):
        self.parser = argparse.ArgumentParser(
            prog=prog,
            description = description,
            )
    def add_positional_arguments(self,*iterables):
        """
        [add arguments to parser]
        """
        for iterable in iterables:
            self.parser.add_argument(
                iterable[0],
                type=iterable[1],
                help=iterable[2],
                default='Null',
            )
    def add_optional_arguments(self,*iterables):
        """
        [add optional arguments to parser]
        """
        for iterable in iterables:
            self.parser.add_argument(
                iterable[0],
                metavar=iterable[1],
                help=iterable[2],
                dest=iterable[3],
                default='Null',
            )
    def get_args(self):
        """
        Returns:
            [args]: [all the args passed]
        """
        return self.parser.parse_args()