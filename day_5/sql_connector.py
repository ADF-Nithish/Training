"""
This file let user to connect the MySQL database.
"""
import datetime
import json
from getpass import getpass
import mysql.connector
from helpers.log_helper import Logging
from helpers.parser import Parser


class SqlConnector:
    """
    [This class is used to open the database and connect the database]
    Attribute :
        conn : connection
    """
    def __init__(self):
        self.__conn = None
        self.__cursor = None
        self.__fields = None
        self.__response_field = None
        self.__response = None
        self.set_fields()
        self.__log = Logging()
        self.__parser = Parser(
            'SqlConnector',
            description='SqlConnector for Python')
        self.__parser.add_positional_arguments(
            ('FirstName',str,'first name of the user'),
            ('LastName',str,'last name of the user'),
            ('DOB',datetime.date.fromisoformat,'Date of Birth'),
            ('Gender',str,'gender of the user'),
            ('National',str,'nationality of the user'),
            ('City',str,'Current city of the user'),
            ('State',str,'State of the user'),
            ('PinCode',int,'pincode of the user'),
            ('Qualification',str,'Qualification of the user'),
            ('Salary',int,'Salary of the user'),
            ('Pan',str,'PAN Number of the user'),)
        self.__parser.add_optional_arguments(
            ('-mN','MiddleName','Middle Name of the user','MiddleName'),)
        self.args = self.__parser.get_args()

    def set_fields(self):
        """sets the field parameter.
        """
        self.__fields = ['id',
        'Request_Received','First_Name','Last_Name','Middle_Name',
        'DOB','Gender','Nationality','City','State','Pincode','Qualification',
        'Salary','PAN_Number']
        self.__response_field = ['id','Request_Id','Response_Generated']
    def execute(self,command):
        """[executes the command]
        """
        self.__cursor.execute(command)

    def create_table_request_info(self):
        """
        Creates Request info table
        """
        table_query = f"""
        Create Table If Not Exists Request_Info(
            {self.__fields[0]} INT AUTO_INCREMENT PRIMARY KEY,
            {self.__fields[1]} TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            {self.__fields[2]} CHAR(30),
            {self.__fields[3]} CHAR(30),
            {self.__fields[4]} CHAR(30) NULL,
            {self.__fields[5]} DATE,
            {self.__fields[6]} CHAR(15),
            {self.__fields[7]} CHAR(30),
            {self.__fields[8]} CHAR(30),
            {self.__fields[9]} CHAR(30),
            {self.__fields[10]} INT(32),
            {self.__fields[11]} CHAR(30),
            {self.__fields[12]} INT(32),
            {self.__fields[13]} VARCHAR(30))
        """
        self.execute(table_query)

    def create_table_response_info(self):
        """
        Creates Table response info
        """
        table_query = f"""
        Create Table If Not Exists Response_Info(
            {self.__response_field[0]} INT PRIMARY KEY AUTO_INCREMENT,
            {self.__response_field[1]} INT,
            {self.__response_field[2]} JSON,
            FOREIGN KEY({self.__response_field[1]}) REFERENCES request_info({self.__response_field[0]})
            )
        """
        self.execute(table_query)

    def insert_into_request_info(self):
        """
        insert values to the table request info
        """
        insert_query = f"""
        Insert into Request_Info 
        (
            {self.__fields[2]},
            {self.__fields[3]},
            {self.__fields[4]},
            {self.__fields[5]},
            {self.__fields[6]},
            {self.__fields[7]},
            {self.__fields[8]},
            {self.__fields[9]},
            {self.__fields[10]},
            {self.__fields[11]},
            {self.__fields[12]},
            {self.__fields[13]})
        values(
            '{self.args.FirstName}',
            '{self.args.LastName}',
            '{self.args.MiddleName}',
            '{self.args.DOB}',
            '{self.args.Gender}',
            '{self.args.National}',
            '{self.args.City}',
            '{self.args.State}',
            '{self.args.PinCode}',
            '{self.args.Qualification}',
            '{self.args.Salary}',
            '{self.args.Pan}')
        """
        self.__log.write_log("Inserted into the table request_info")
        self.execute(insert_query)

    def insert_into_response_info(self,request_id,response):
        """
        insert values to the table request info
        """
        insert_query = f"""
        Insert into Response_Info 
        (
            {self.__response_field[1]},
            {self.__response_field[2]}    
        )
        values(
            '{request_id}',
            '{response}'
        )
        """ if request_id is not None else f"""
        Insert into Response_Info 
        (
            {self.__response_field[2]}    
        )
        values(
            '{response}'
        )
        """
        self.__log.write_log("Inserted into the table response_info")
        self.execute(insert_query)
    def open_connection(self):
        """
        [opens connection]
        """
        try:
            self.__conn = mysql.connector.connect(
                host='127.0.0.1',
                user='adf',
                password=getpass('Enter password:'),
                database='adf',
                autocommit=True,
            )
            self.__cursor = self.__conn.cursor()
            self.__log.write_log("Connection is successful.")
            print("Connecting to the default database adf.......")
        except mysql.connector.Error as error:
            print("Error: ",error)

    def __age_calculate(self):
        try:
            today = datetime.date.today()
            birth_date = datetime.date(*list(map(int,str(self.args.DOB).split('-'))))
            age = today.year - birth_date.year - (
                (today.month, today.day) < (birth_date.month, birth_date.day))
        except (Exception,IndexError) as error:
            self.__log.write_log(error)
        if (age >= 21 and self.args.Gender == 'Male') or (
            age >= 18 and self.args.Gender == 'Female'):
            self.__log.write_log("Age Validation is Successful")
            return True
        self.__log.write_log("Age Validation Error")
        return False
    def __is_user_repeated(self):
        try:
            required_query = f"""
            select request_received from request_info where Pan_Number = '{self.args.Pan}';
            """
            self.execute(required_query)
            today = datetime.date.today()
            objects_received = self.__cursor.fetchall()
        except Exception as error:
            self.__log.write_log(error)
        if len(objects_received) == 0 or today.day - int(
            str(*objects_received[-1]).split(' ')[0].split('-')[2]) > 5 :
            self.__log.write_log("User Repeated Validation is Successful")
            return True
        self.__log.write_log("User Repeated Validation Error")
        return False
    def __is_indian_or_american(self):
        if self.args.National.lower() == 'india' or self.args.National.lower() == 'america':
            self.__log.write_log("Nationality Validation is Successful")
            return True
        self.__log.write_log("Nationality Validation Error")
        return False
    def __check_state(self):
        states = ['andhra_pradesh','arunachal_pradesh',
        'assam','bihar','chhattisgarh','karnataka','madhya_pradesh','odisha',
        'tamil_nadu','telangana','west_bengal']
        if self.args.State.lower() in states:
            self.__log.write_log("State Validation is Successful")
            return True
        self.__log.write_log("State Validation Error")
        return False
    def __check_salary(self):
        if int(self.args.Salary) > 10000 and int(self.args.Salary < 90000):
            self.__log.write_log("Salary Validation is Successful")
            return True
        self.__log.write_log("Salary Validation Error")
        return False
    def validate(self):
        """[Used To validate the eligibility criteria]

        Returns:
            True if satisfying else False
        """
        try:
            assert self.__age_calculate() is True, Exception('Age is less than expected')
            assert self.__is_user_repeated() is True,Exception(
                'Recently request received in last 5 days')
            assert self.__is_indian_or_american() is True, Exception(
                'Nationality should be india or america')
            assert self.__check_state() is True, Exception('State should be valid')
            assert self.__check_salary() is True, Exception(
                'Salary should be below 90k and above 10k')
            self.__log.write_log("All Validation is Successful")
            self.__response = {'response':'success'}
            return True
        except AssertionError as error:
            self.__response = {'response':f"{error}"}
            self.__log.write_log("Validation Error...Check the Eligibility Criteria...")
            return False
    def get_response(self):
        """return response
        """
        return self.__response

s = SqlConnector()
s.open_connection()
s.create_table_request_info()
# s.create_table_response_info()
try:
    assert s.validate() is True
    s.insert_into_request_info()
except AssertionError:
    pass

# s.insert_into_response_info(1,json.dumps(s.get_response()))
