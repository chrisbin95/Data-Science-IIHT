#### <div align="center">Python Worksheet 2022</div>
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
</div>

<br/>

# Challenge 1: To create a Book Library using Array List and search function
### Problem Statement: How to create a book library using array list with search function?

>- Python
```python
class Library(object):
    books=[]
    author=[]
    price=[]
    def __init__(self,name,author,isbn,price):
        self.name=name
        self.author=author
        self.isbn=isbn
        self.price=price
    def addBook(self):
        Library.books.append((self.name,self.author,self.isbn,self.price))
    def searchBookisbn(self,isbn):
        for book in Library.books:
            if book[2]==isbn:
                return book
    def searchBookAuthor(self,author):
        for book in Library.books:
            if book[1]==author:
                Library.author.append(book)
                return Library.author
    def searchUnderPrice(self,price):
        for book in Library.books:
            if book[3]==price:
                Library.price.append(book)
                return Library.price
book=Library('Great Expectations','Charles Dick','ID0234',300)
book.addBook()
book=Library('War and Peace','Leo Tolstoy','ID278',250)
book.addBook()
book=Library('Middlemarch','George Eliot','ID345',400)
book.addBook()
print(book.searchBookisbn('ID278'))
print(book.searchBookAuthor('George Eliot'))
print(book.searchUnderPrice(400))
```
<br/>

# Challenge 2: To Append Your Name with a text
### Problem Statement: How to append your name with a custom text?

>- Python
```python
class hello:
    def func1(self,name):
        print(f"hello,{name}")
        return name
b=hello()
x=input("Enter the name:")
b.func1(x)
```
<br/>

# Challenge 3: To Create Employee Details List
### Problem Statement: How to create an employee details list?

>- Python
```python
class samp:
    def __init__(self,name,age,id,salary):
        self.name= name
        self.age= age
        self.id= id
        self.salary= salary
emp1= samp('faker',24,'id33',25000)
emp2= samp('joker',25,'id32',30000)
print(emp1.__dict__)
print(emp2.__dict__)
print(emp1.name)
print(emp2.age)
print(emp2.__init__)
```
<br/>

# Challenge 4: To Find complex number of given inputs
### Problem Statement: How to find the complex number of given inputs?

>- Python
```python
class complexno:
    def __init__(self,r=0,i=0):
        self.real=r
        self.imag=i
    def get(self):
        print("{0}+{1}j".format(self.real,self.imag))
x=float(input("Enter a real no:"))
y=float(input("Enter an imaginary no:"))
c1= complexno(x,y)
c1.get()
c2= complexno(y)
c2.var= 10
print((c2.real, c2.imag, c2.var))
print(c2.var)
```
<br/>

# Challenge 5: To Create a Digital Speedometer to Record Accelertion and Braking Speed
### Problem Statement: How to create a digital speedometer and record data of a vehicle's accelertion and braking speed?

>- Python
```python
class car:
    def __init__(self,year,mph,speed):
        self.year=year
        self.mph=mph
        self.speed=speed
    def accelerate(self,speed):
        for i in range(speed,121,10):
                print("accelerating speed:",i)
    def brake(self,speed):
        for x in range(speed,10,-20):
            print("braking speed:",x)  
c1=car(2014,58,60)
print('year ',c1.year)
print('mph ',c1.mph)
print('speed ',c1.speed)
c1.accelerate(10)
c1.brake(120)
```
<br/>

# Challenge 6: To Calculate Revenue per Employee along with Turn-over data in a system
### Problem Statement: How to calculate revenue per employee with regards to turn-over data?

>- Python
```python
class company:
    def __init__(self,name,turn,rev,eno):
        self.name= name
        self.turn=turn
        self.rev=rev
        self.eno=eno
    def revenue(self):
        i=self.rev/self.eno
        print('\n Revenue per employee is:',i)
x=input("NAME:")
y=int(input("TURN-OVER:"))
z=int(input("REVENUE:"))
a=int(input("NO: OF EMPLOYEES:"))
c=company(x,y,z,a)
c.revenue()
```
<br/>

# Challenge 7: To Create an Array of elements and to pass a value from function
### Problem Statement: How to perform array manipulation (Pass element from function to array)?

>- Python
```python
def change(var, list):
    var=1
    list[3]=40
k=4
a=[1,2,3,4]
print(a);
change(k, a)
print(change)
print(a);
```
<br/>

# Challenge 8: To Calculate Area and Perimeter of a rectangle
### Problem Statement: How to calculate the area and perimeter of a rectangle?

>- Python
```python
class rect:
    def __init__(self,length,width):
        
        self.length=length
        self.width=width
    def cal(self):
        return self.length*self.width
    def cal1(self):
        return (2*(self.length+self.width))
c=rect(3,4)
print('Area of the Rectangle',c.cal())
print('Perimeter of the Rectangle',c.cal1())
```
<br/>

# Challenge 9: To Append Integers into List using a Class
### Problem Statement: How to append integers into list using class & function with exception handlers?

>- Python
```python
class samp:
    def __init__(self):
        self.smp=read(self)
def read(lst):
    lst=[]
    try:
        for i in range(1,6):
            lst.append((input('Enter:')))        
    except ValueError:
            print(lst,'contains string!Run again.')
    print("list of 5 integers:",lst)    
samp()
read(int) 
```
<br/>

# Challenge 10: To invoke list operations
### Problem Statement: How to handle list operations in python?

>- Python
```python
i=[1,2,3]
j=[4,5,6]
k=len(i)
print(k)
print(i)
i.remove(1)
print(i)
i.pop(0)
print(i)
i.append
```
<br/>

# Challenge 11: To handle loop functions
### Problem Statement: How to operate loop's in python?

>- Python
```python
class looping:
        for i in range(1,11):
            print(i,"",i+10,"",i*100,'',i*1000)
l=looping()
```
<br/>

# Challenge 12: To handle file operations
### Problem Statement: How to open a text file and write to it in python?

>- Python
```python
import os
os.chdir('C:\python')
a=open('sam1.txt','w+')
for i in range(10):
    a.write("This is a new txt file %d\n\r" %(i+1))
a=open('sam1.txt','r')
x=a.read()
print(x)
```
<br/>

# Challenge 13: To open and read a csv in python console
### Problem Statement: How to open a csv file & read it with python?

>- Python
```python
import csv
import os
os.chdir('C:\pyf')
with open('sample1.csv','r') as File:
    read=csv.reader(File)
    #next(read) #read next line
    for a in File:
        print(a)
```
<br/>

# Challenge 14: To read a csv in python 
### Problem Statement: How to open a csv file; read & write to it with python?

>- Python
```python
import csv
import os
os.chdir('C:\pyf')
with open('sample1.csv','r+') as f:
    r=csv.reader(f)
    with open('hello.csv','w') as new:
        w=csv.writer(new, delimiter='-')
        for line in r:
            w.writerow(line)
```
<br/>


## Acknowledgement

- Fork the Repo and use spyder IDE for training 
- This markdown file _(.md)_ includes code to `Python Challenges`. You can use it for reference.
- Once you've added the zip file to downloads, download spyder or use online compilers to work with it.
- A open pull request is considered as successful submission. Check for `debugging` errors
- Consider Like and follow for more updates!
<div align="center">&copy; | 2021 - 2022</div>
