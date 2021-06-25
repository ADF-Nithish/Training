"""
This file let user to connect the MySQL database.
"""
import os
import mysql.connector
from helpers.log_helper import Logging
from helpers.write_config import WriteConfig
from helpers.parser import Parser


class SqlConnector:
    """
    [This class is used to open the database and connect the database]
    Attribute :
        conn : connection
    """
    def __init__(self):
        self.__conn = None
        self.__parser = Parser(
            'SqlConnector',
            description='SqlConnector for Python')
        self.__parser.add_argument(
            '-database',
            metavar='str',
            specific_help='database name')
        self.args = self.__parser.get_args().database

    def open_connection(self):
        """
        [opens connection]
        """
        try:
            with mysql.connector.connect(
                host='127.0.0.1:3306',
                user='adf',
                password='adf@123',
            ) as self.__conn:
                print(self.__conn)
        except mysql.connector.Error as error:
            print("Error: ",error)

s = SqlConnector()
print(s.args)