## Python Exercise -2021-06-18

### Exercise-1.py
#### Problem Statement :
   Program to read a file and store the unique words in a list sorted based on the length of word in a new file along with each word length appended to it.
#### Solution Approach :
  - First try to open the [text file](https://github.com/ADF-Nithish/Training/blob/master/Python%20Exercises%20-%202021-06-18/Exercise-1/Exercise-1.txt) with the built-in ```open()``` function using ```try``` block
  - Next, Read the stream using ```read()``` function and store all the words in a list.
  - Also catch the **FileNotFoundException** with a ```except``` block.
  - Next, find all the unique elements in a list by taking the count of a word in the list and sort it by using the length of a word as a ```key``` in a ```lambda``` function.
  - Next, write the above calculated list into a new file by creating it with ```open()``` function.
#### FlowChart: 
  ![Image](https://github.com/ADF-Nithish/Training/blob/master/Python%20Exercises%20-%202021-06-18/Exercise-1/Exercise-1-Flowchart.png)
#### Execution of the File with Command Line Arguements:
```python
python3 Exercise-1.py Exercise-1.txt Exercise-1-ans.txt
```
#### Output:
```
test. 5
test-2. 7
test-3. 7
```


### Exercise-2.py
#### Problem Statement :
   Program to read a CSV (CSV with n number of columns) and store it in DICT of list.
#### Solution Approach :
  - First try to open the [csv file](https://github.com/ADF-Nithish/Training/blob/master/Python%20Exercises%20-%202021-06-18/Exercise-2/Exercise-2.csv) with the built-in ```open()``` function using ```try``` block.
  - Also catch the **FileNotFoundException** with a ```except``` block.
  - Next, Read the stream using ```readline()``` function.
  - Create a dictionary and store the colums as a key with empty list as a value.
  - Next, read all the stream using ```readline()``` function and append all the values to the dict for a separate key.
  - Next, output all the dict of list to the console.
#### FlowChart: 
  ![Image](https://github.com/ADF-Nithish/Training/blob/master/Python%20Exercises%20-%202021-06-18/Exercise-2/Exercise-2-Flowchart.png)
#### Execution of the File with Command Line Arguements:
```python
python3 Exercise-2.py Exercise-2.csv
```
#### Output:
```
{'venue_id': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '37', '38'], 'venue': ['Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium', 'Sharjah Cricket Stadium', 'JSCA International Stadium Complex', 'Saurashtra Cricket Association Stadium', 'Shaheed Veer Narayan Singh International Stadium', 'Maharashtra Cricket Association Stadium', 'Subrata Roy Sahara Stadium', "St George's Park", '"Vidarbha 
Cricket Association Stadium Jamtha"', 'Brabourne Stadium', 'Dr DY Patil Sports Academy', 'Wankhede Stadium', 'Eden Gardens', 'Nehru Stadium', 'De Beers Diamond Oval', 'Green Park', 'New Wanderers Stadium', 'Sawai Mansingh Stadium', 'Holkar Cricket Stadium', '"Rajiv Gandhi International Stadium Uppal"', 'Buffalo Park', 'Kingsmead', 'Dubai 
International Cricket Stadium', 'Himachal Pradesh Cricket Association Stadium', 'Feroz Shah Kotla', 'Barabati Stadium', '"MA Chidambaram Stadium Chepauk"', '"Punjab Cricket Association IS Bindra Stadium  
Mohali"', '"Punjab Cricket Association Stadium Mohali"', 'SuperSport Park', 'Newlands', 'OUTsurance Oval', 'M.Chinnaswamy Stadium', '"Sardar Patel Stadium Motera"', 'Sheikh Zayed Stadium'], 'city': ['Visakhapatnam', 'Sharjah', 'Ranchi', 'Rajkot', 'Raipur', 'Pune', 'Pune', 'Port Elizabeth', 'Nagpur', 'Mumbai', 'Mumbai', 'Mumbai', 'Kolkata', 'Kochi', 'Kimberley', 'Kanpur', 'Johannesburg', 'Jaipur', 'Indore', 'Hyderabad', 'East London', 'Durban', 'Dubai', 'Dharamsala', 'Delhi', 'Cuttack', 'Chennai', 'Chandigarh', 'Chandigarh', 'Centurion', 'Cape Town', 'Bloemfontein', 'Bengaluru', 'Ahmedabad', 'Abu Dhabi']} 
```


### Exercise-3.py
#### Problem Statement :
   Program to Print all Prime Numbers in an Interval of 5 seconds
#### Solution Approach :
  - First calculate the current time into a variable starttime using ```time``` module.
  - Initialize num value to 3(as prime number starts from 3).
  - Next, check if the num is prime or not by dividing it from 2 to the num itself.
  - Now, calculate the current time and take difference with startime to check if the time exceeds 5 seconds.
#### FlowChart: 
  ![Image](https://github.com/ADF-Nithish/Training/blob/master/Python%20Exercises%20-%202021-06-18/Exercise-3/Exercise-3-Flowchart.png)
#### Execution of the File with Command Line Arguements:
```python
python3 Exercise-3.py
```


### Exercise-4.py
#### Problem Statement :
   Program to Find HCF or GCD
#### Solution Approach :
  - First, Input the list of numbers to find GCD or HCF.
  - Next, store the first value in the list to gcd variable.
  - Now calculate gcd of two number (gcd,list[i]) by Euclidian's theorem.
  - Repeat till last element to find the gcd value.
#### FlowChart: 
  ![Image](https://github.com/ADF-Nithish/Training/blob/master/Python%20Exercises%20-%202021-06-18/Exercise-4/Exercise-4-Flowchart.png)
#### Execution of the File with Command Line Arguements:
```python
python3 Exercise-4.py 4 8 16 32
```
#### Output:
```
4
```


### Exercise-5.py
#### Problem Statement :
   Program to Convert Decimal to Binary, Octal and Hexadecimal
#### Solution Approach :
  - First store the decimal value in a variable.
  - using python's inbuilt functions ```bin()``` ```oct()``` and ```hex()```, we can calculate all the binary,octal and hexadecimal value of a decimal.
#### FlowChart: 
  ![Image](https://github.com/ADF-Nithish/Training/blob/master/Python%20Exercises%20-%202021-06-18/Exercise-5/Exercise-5-Flowchart.png)
#### Execution of the File with Command Line Arguements:
```python
python3 Exercise-5.py 4
```
#### Output:
```
Binary of 4 - 100
Octal of 4 - 4
HexaDecimal of 4 - 4
```


### Exercise-6.py
#### Problem Statement :
   Program to Find ASCII Value of Character.
#### Solution Approach :
  - First, store the char value in a variable.
  - return the ASCII value of a char using python's built-in function ```ord()```.
#### FlowChart: 
  ![Image](https://github.com/ADF-Nithish/Training/blob/master/Python%20Exercises%20-%202021-06-18/Exercise-6/Exercise-6-Flowchart.png)
#### Execution of the File with Command Line Arguements:
```python
python3 Exercise-6.py b
```
#### Output:
```
98
```


### Exercise-7.py
#### Problem Statement :
  Program to get an application (name , age , gender, salary, state, city)
#### Solution Approach :
  - First Create a class Application with name, age, gender, salary, state, city as a private attributes of the class.
  - return all the values using Application's object using ```__repr__()``` function.
#### FlowChart: 
  ![Image](https://github.com/ADF-Nithish/Training/blob/master/Python%20Exercises%20-%202021-06-18/Exercise-7/Exercise-7-Flowchart.png)
#### Execution of the File with Command Line Arguements:
```python
python3 Exercise-7.py Nithish 20 Male 18000 Tamilnadu Coimbatore
```
#### Output:
```
Application(Name: Nithish , Age: 20 , Gender: Male , Salary: 18000 , State: Tamilnadu , City: Coimbatore)
```
