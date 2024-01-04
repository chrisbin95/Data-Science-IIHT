#### <div align="center"> &#10024; Python Worksheet &#10024;</div>
<div align="center"><img src=https://twilio-cms-prod.s3.amazonaws.com/original_images/header.gif alt=python-ide style="padding:5px;margin:10px;width:35%;"/></div>
<br/>
<div align="center">
<a href="https://linkedin.com/in/chrisbin-thomas-334744195" target="_blank">
<img src=https://img.shields.io/badge/linkedin-%231E77B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white alt=linkedin style="margin-bottom: 10px;" />
</a>
<a href="https://github.com/chrisbin95" target="_blank">
<img src=https://img.shields.io/badge/github-%2324292e.svg?&style=for-the-badge&logo=github&logoColor=white alt=github style="margin-bottom: 10px;" />
</a>  
<a href="https://github.com/chrisbin95/Data-Science-IIHT" target="_blank">
<img src=https://franchisebyte.com/wp-content/uploads/2020/11/IIHT-Franchise-Logo.png alt=iiht style="width:70px;height:28px;margin-bottom: 10px;" />
</a>  
<a href="https://chrisbin95.github.io/Portfolio" target="_blank">
<img src=https://user-images.githubusercontent.com/41782385/59523230-55488280-8f03-11e9-9abe-e8e0f3d9a245.gif alt=py style="width:30px;margin-bottom: 10px;" />
</a> 
</div>

<br/>

# Challenge 1: To create a Book Library using Array List and search function
### Problem Statement: How to create a book library using array list with search function?

>- Python
```python
class Library(object):
    books = []

    def __init__(self, name, author, isbn, price):
        self.name = name
        self.author = author
        self.isbn = isbn
        self.price = price

    def addBook(self):
        Library.books.append((self.name, self.author, self.isbn, self.price))

    def searchBookisbn(self, isbn):
        for book in Library.books:
            if book[2] == isbn:
                return book
        return None  # Return None if the book with the given ISBN is not found

    def searchBookAuthor(self, author):
        author_books = []
        for book in Library.books:
            if book[1] == author:
                author_books.append(book)
        return author_books

    def searchUnderPrice(self, price):
        price_books = []
        for book in Library.books:
            if book[3] == price:
                price_books.append(book)
        return price_books


# Create instances of the Library class
library = Library('Great Expectations', 'Charles Dick', 'ID0234', 300)
library.addBook()

library = Library('War and Peace', 'Leo Tolstoy', 'ID278', 250)
library.addBook()

library = Library('Middlemarch', 'George Eliot', 'ID345', 400)
library.addBook()

# Create a new instance for searching
search_instance = Library('', '', '', '')

print(search_instance.searchBookisbn('ID278'))
print(search_instance.searchBookAuthor('George Eliot'))
print(search_instance.searchUnderPrice(400))
```
<br/>

# Challenge 2: To Append Your Name with a text
### Problem Statement: How to append your name with a custom text?

>- Python
```python
class Hello:
    def func1(self, name):
        print(f"Hello, {name}")
        return name

# Create an instance of the Hello class
b = Hello()

# Get input from the user
x = input("Enter the name: ")

# Call the func1 method and capture the returned value
result = b.func1(x)

# Print the returned value
print(f"Returned value: {result}")
```
<br/>

# Challenge 3: To Create Employee Details List
### Problem Statement: How to create an employee details list?

>- Python
```python
class Samp:
    def __init__(self, name, age, emp_id, salary):  # Changed "id" to "emp_id" for clarity
        self.name = name
        self.age = age
        self.emp_id = emp_id  # Changed to "emp_id" for clarity
        self.salary = salary

# Create instances of the Samp class
emp1 = Samp('faker', 24, 'id33', 25000)
emp2 = Samp('joker', 25, 'id32', 30000)

# Print the dictionary representation of each instance
print(emp1.__dict__)
print(emp2.__dict__)

# Access individual attributes
print(emp1.name)
print(emp2.age)

# Note: "__init__" is not something you usually access directly.
# Instead, it's called automatically when you create an instance.
# If you want to check the type of the constructor, use the type() function.
print(type(emp1.__init__))
```
<br/>

# Challenge 4: To Find complex number of given inputs
### Problem Statement: How to find the complex number of given inputs?

>- Python
```python
class ComplexNo:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get(self):
        print("{0}+{1}j".format(self.real, self.imag))

# Get input from the user
x = float(input("Enter a real no: "))
y = float(input("Enter an imaginary no: "))

# Create instances of the ComplexNo class
c1 = ComplexNo(x, y)
c1.get()

c2 = ComplexNo(y)
c2.var = 10  # Add var as an attribute to c2 instance

# Access and print attributes
print((c2.real, c2.imag, getattr(c2, 'var', None)))  # Use getattr to avoid AttributeError
print(c2.var if hasattr(c2, 'var') else None)  # Check if 'var' exists before accessing
```
<br/>

# Challenge 5: To Create a Digital Speedometer to Record Accelertion and Braking Speed
### Problem Statement: How to create a digital speedometer and record data of a vehicle's accelertion and braking speed?

>- Python
```python
class Car:
    def __init__(self, year, mph, speed):
        self.year = year
        self.mph = mph
        self.speed = speed

    def accelerate(self, speed_increase):
        for i in range(self.speed, self.speed + speed_increase + 1, 10):
            print("Accelerating speed:", i)
        self.speed += speed_increase

    def brake(self, speed_decrease):
        for x in range(self.speed, max(self.speed - speed_decrease - 1, 0), -20):
            print("Braking speed:", x)
        self.speed = max(self.speed - speed_decrease, 0)

# Create an instance of the Car class
c1 = Car(2014, 58, 60)

# Access and print attributes
print('Year:', c1.year)
print('MPH:', c1.mph)
print('Speed:', c1.speed)

# Accelerate and brake
c1.accelerate(10)
c1.brake(120)
```
<br/>

# Challenge 6: To Calculate Revenue per Employee along with Turn-over data in a system
### Problem Statement: How to calculate revenue per employee with regards to turn-over data?

>- Python
```python
class Company:
    def __init__(self, name, turn, rev, eno):
        self.name = name
        self.turn = turn
        self.rev = rev
        self.eno = eno

    def revenue(self):
        i = self.rev / self.eno
        print('\nRevenue per employee is:', i)

# Get input from the user
name_input = input("NAME: ")
turnover_input = int(input("TURN-OVER: "))
revenue_input = int(input("REVENUE: "))
employees_input = int(input("NO: OF EMPLOYEES: "))

# Create an instance of the Company class
company_instance = Company(name_input, turnover_input, revenue_input, employees_input)

# Call the revenue method
company_instance.revenue()
```
<br/>

# Challenge 7: To Create an Array of elements and to pass a value from function
### Problem Statement: How to perform array manipulation (Pass element from function to array)?

>- Python
```python
def change(var, lst):  # Avoid using 'list' as a variable name, as it's a built-in type
    var = 1
    lst[3] = 40

k = 4
a = [1, 2, 3, 4]

print("Original list:", a)
change(k, a)
print("Modified list:", a)
```
<br/>

# Challenge 8: To Calculate Area and Perimeter of a rectangle
### Problem Statement: How to calculate the area and perimeter of a rectangle?

>- Python
```python
class Rect:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def cal(self):
        return self.length * self.width

    def cal1(self):
        return 2 * (self.length + self.width)

# Create an instance of the Rect class
c = Rect(3, 4)

# Calculate and print the area and perimeter
print('Area of the Rectangle:', c.cal())
print('Perimeter of the Rectangle:', c.cal1())
```
<br/>

# Challenge 9: To Append Integers into List using a Class
### Problem Statement: How to append integers into list using class & function with exception handlers?

>- Python
```python
class Samp:
    def __init__(self):
        self.smp = self.read()

    def read(self):
        lst = []
        try:
            for i in range(1, 6):
                lst.append(int(input('Enter an integer: ')))
        except ValueError:
            print('Input contains a non-integer! Run again.')
        print("List of 5 integers:", lst)
        return lst

# Create an instance of the Samp class
s = Samp() 
```
<br/>

# Challenge 10: To invoke list operations
### Problem Statement: How to handle list operations in python?

>- Python
```python
i = [1, 2, 3]
j = [4, 5, 6]
k = len(i)

print("Length of i:", k)
print("Original list i:", i)

# Remove the element '1' from the list
i.remove(1)
print("List i after removing element '1':", i)

# Remove the element at index 0 from the list
i.pop(0)
print("List i after popping element at index 0:", i)

# Append a new element to the list
i.append(7)
print("List i after appending '7':", i)
```
<br/>

# Challenge 11: To handle loop functions
### Problem Statement: How to operate loop's in python?

>- Python
```python
class Looping:
    def print_numbers(self):
        for i in range(1, 11):
            print(i, "", i + 10, "", i * 100, '', i * 1000)

# Create an instance of the Looping class
l = Looping()

# Call the print_numbers method
l.print_numbers()
```
<br/>

# Challenge 12: To handle file operations
### Problem Statement: How to open a text file and write to it in python?

>- Python
```python
import os

# Use double backslashes or a raw string for the path
os.chdir('C:\\python')

# Open a file for writing and reading
a = open('sam1.txt', 'w+')

# Write to the file
for i in range(10):
    a.write("This is a new txt file %d\n\r" % (i + 1))

# Close the file
a.close()

# Open the file for reading
a = open('sam1.txt', 'r')

# Read and print the contents
x = a.read()
print(x)

# Close the file
a.close()
```
<br/>

# Challenge 13: To open and read a csv in python console
### Problem Statement: How to open a csv file & read it with python?

>- Python
```python
import csv
import os

# Set the working directory
os.chdir('C:\\pyf')

# Open the CSV file for reading
with open('sample1.csv', 'r') as file:
    # Create a CSV reader
    reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in reader:
        print(row)
```
<br/>

# Challenge 14: To read a csv in python 
### Problem Statement: How to open a csv file; read & write to it with python?

>- Python
```python
import csv
import os

# Set the working directory
os.chdir('C:\\pyf')

with open('sample1.csv', 'r') as f:
    r = csv.reader(f)

    with open('hello.csv', 'w', newline='') as new:
        w = csv.writer(new, delimiter='-')

        for line in r:
            w.writerow(line)
```
<br/>

# Challenge 15: Basic operations
### Problem Statement: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5. 
The numbers obtained should be printed in a comma-separated sequence on a single line.
#### Hints: Consider use range(#begin, #end) method

>- Python
```python
l = []

for i in range(10, 100):
    if (i % 7 == 0) and (i % 5 != 0):
        l.append(str(i))

result = ', '.join(l) + '.'
print(result)
```
<br/>

# Challenge 16: Basic operations
### Problem Statement: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320.
#### Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

>- Python
```python
def fact(x):
    if x < 0:
        return "Factorial is not defined for negative numbers."
    elif x == 0:
        return 1
    else:
        return x * fact(x - 1)

try:
    x = int(input("Enter a non-negative integer: "))
    print(f"The factorial of {x} is: {fact(x)}")
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")
```
<br/>

# Challenge 17: Basic operations
### Problem Statement: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} .
#### Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider use dict()

>- Python
```python
try:
    n = int(input('Enter a non-negative integer: '))
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        d = {i: i*i for i in range(1, n+1)}
        print(d)
except ValueError:
    print("Invalid input. Please enter a non-negative integer.")
```
<br/>

# Challenge 18: Basic operations
### Problem Statement: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98') .
#### Hints: In case of input data being supplied to the question, it should be assumed to be a console input. tuple() method can convert list to tuple

>- Python
```python
values = input("Enter comma-separated values: ")
l = [value.strip() for value in values.split(",")]
t = tuple(l)

print("List:", l)
print("Tuple:", t)
```
<br/>

# Challenge 19: Basic operations
### Problem Statement: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods.
#### Hints: Use init method to construct some parameters

>- Python
```python
class InputOutString(object):
    def __init__(self, input_string=""):
        self.s = input_string

    def printString(self):
        print(self.s.upper())

# Get input string from the user
user_input = input('Enter a string: ')

# Create an instance of the class with the user input
strObj = InputOutString(user_input)

# Print the string in uppercase
strObj.printString()
```
<br/>

# Challenge 20: Basic operations
### Problem Statement: Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 The output of the program should be: 18,22,24 .
#### Hints: If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26) In case of input data being supplied to the question, it should be assumed to be a console input.

>- Python
```python
import math

# Take input for c and h
c = float(input("Enter value for c: "))
h = float(input("Enter value for h: "))

# Take a comma-separated list of values
items = [float(x) for x in input("Enter comma-separated values: ").split(',')]

# Calculate the rounded square root for each value
values = [str(int(round(math.sqrt(2 * c * d / h)))) for d in items]

# Print the result
print(','.join(values))
```
<br/>

# Challenge 21: Basic operations
### Problem Statement: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given to the program: 3,5 Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] .
#### Hints: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

>- Python
```python
input_str = "3,5"  # Using a string for input
dimensions = [int(x) for x in input_str.split(',')]
row_num = dimensions[0]
col_num = dimensions[1]

multilist = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        multilist[row][col] = row * col

print(multilist)
```
<br/>

# Challenge 22: Basic operations
### Problem Statement: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically. Suppose the following input is supplied to the program: without,hello,bag,world Then, the output should be: bag,hello,without,world.
#### Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

>- Python
```python
items = input("Enter comma-separated items: ").split(',')
items.sort()
print(','.join(items))
```
<br/>

# Challenge 23: Basic operations
### Problem Statement: Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. Suppose the following input is supplied to the program: Hello world Practice makes perfect Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT.
#### Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

>- Python
```python
lines = []

while True:
    s = input(">>> ")
    if not s:
        break
    lines.append(s.upper())

for sentence in lines:
    print(sentence)
```
<br/>

# Challenge 24: Basic operations
### Problem Statement: Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again Then, the output should be: again and hello makes perfect practice world.
#### Hints: In case of input data being supplied to the question, it should be assumed to be a console input. We use set container to remove duplicated data automatically and then use sorted() to sort the data.

>- Python
```python
s = input('>>>')
unique_sorted_words = ' '.join(sorted(set(s.split())))
print(unique_sorted_words)
```
<br/>

# Challenge 25: Basic operations
### Problem Statement: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence. Example: 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.
#### Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

>- Python
```python
binary_input = input('>>>')
binary_numbers = [x for x in binary_input.split(',') if int(x, 2) % 5 == 0]
print(','.join(binary_numbers))
```
<br/>

# Challenge 26: Advanced operations
### Problem Statement: Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. Suppose the following input is supplied to the program: 9 Then, the output should be: 11106.
#### Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

>- Python
```python
a = input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print(n1+n2+n3+n4)

#(or)

a = input()
total_sum = 0

for i in range(1, 5):
    total_sum += int(str(a) * i)

print(total_sum)
```
<br/>

# Challenge 27: Advanced operations
### Problem Statement: Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9 Then, the output should be: 1,3,5,7,9.
#### Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

>- Python
```python
try:
    values = input("Enter comma-separated numbers: ")
    numbers = [x for x in values.split(",") if int(x) % 2 != 0]
    print(",".join(numbers))
except ValueError:
    print("Invalid input. Please enter integer values.")
```
<br/>

# Challenge 28: Advanced operations
### Problem Statement: Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following: D 100 W 200 D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500 .
#### Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

>- Python
```python
netAmount = 0

while True:
    s = input("Enter transaction (D/W amount) or press Enter to finish: ")
    if not s:
        break

    values = s.split(" ")
    
    if len(values) == 2:
        operation = values[0]
        try:
            amount = int(values[1])
            if operation == "D":
                netAmount += amount
            elif operation == "W":
                netAmount -= amount
            else:
                print("Invalid operation. Please enter 'D' or 'W'.")
        except ValueError:
            print("Invalid amount. Please enter a valid integer.")
    else:
        print("Invalid input. Please enter a valid transaction.")

print("Net Amount:", netAmount)
```
<br/>

# Challenge 29: Advanced operations
### Problem Statement: A website requires the users to input username and password to register. Write a program to check the validity of password input by users. Following are the criteria for checking the password:
#### At least 1 letter between [a-z]
#### At least 1 number between [0-9]
#### At least 1 letter between [A-Z]
#### At least 1 character from [$#@]
#### Minimum length of transaction password: 6
### Maximum length of transaction password: 12 Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma. Example If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1.
#### Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

>- Python
```python
import re
value = []
items=[x for x in input('>>>').split(',')]
for p in items:
    if len(p)<=6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))

#(or)

import re

def is_valid_password(password):
    if 6 <= len(password) <= 12 and re.match("^[a-zA-Z0-9$#@]+$", password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(c.isupper() for c in password) and any(c in '$#@' for c in password):
        return True
    return False

items = [x for x in input('Enter passwords separated by commas: ').split(',')]
valid_passwords = [p for p in items if is_valid_password(p)]

print("Valid passwords:", ",".join(valid_passwords))
```
<br/>

# Challenge 30: Advanced operations
### Problem Statement: Write a program that computes the Normal Distribution of inputs and plot the data using seaborn module.
#### Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

>- Python
```python

import numpy as np
from scipy.stats import norm
import seaborn as sns

# Example 1
print(sum(range(4), -1))  # Output: 6

# Example 2
# Generate random samples from a normal distribution
data_normal = norm.rvs(size=10000, loc=0, scale=1)

# Create a histogram with KDE using seaborn
ax = sns.distplot(data_normal, bins=100, kde=True, color='skyblue',
                  hist_kws={"linewidth": 15, 'alpha': 1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')
```
<br/>


## ```Acknowledgement```
#### Thankyou for the ⭐ on the repository. If not, do starring! ✌
- Fork the Repo and use spyder IDE (or) [https://replit.com/languages/online-python-compiler](Replit) for training 
- This markdown file _(.md)_ includes code to `Python Challenges`. You can use it for reference.
- Once you've added the zip file to downloads, Recommended Use of : `Anaconda Spyder`, `CodePen`, `Programiz` or `Online Python` Interpreter's to work with it.
- A open pull request is considered as successful and forking is mandatory. Check & `debug` errors on Interpreter Console.
- Consider Like and Follow 🌟 for more updates!
### <div align="center"> &copy; | 2021 - 2022 </div>
