""" [File used to write config]

    Returns:
        [log]: [Logging]
"""
import os
from helpers.log_helper import Logging

class WriteConfig:
    """
    Config file operations are done using this class
    """
    def __init__(self) -> None:
        self.__config = os.path.join(os.getcwd(),'.config')
        self.__log = Logging()

    def get_config(self):
        """
        return if config file.
        """
        return self.__config
    def write_config(self):
        """
        writes into config file.
        """
        pass
