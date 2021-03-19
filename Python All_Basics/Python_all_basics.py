>>>.py <- Save extension! 
>>> Copyright © from AICTE <<<

>>>#Create a Book Library using Array Lists!

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

>>>#Function Usage in py.

class hello:
    def func1(self,name):
        print(f"hello,{name}")
        return name
b=hello()
x=input("Enter the name:")
b.func1(x)

>>>#Employee Details

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

>>>#Complex Number (Math)

class complexno:
    def __init__(self,r=0,i=0):
        self.real=r
        self.imag=i
    def get(self):
        print("{0}+{1}j".format(self.real,self.imag))
x=float(input("Enter the real no:"))
y=float(input("Enter the imag no:"))
c1= complexno(x,y)
c1.get()
c2= complexno(y)
c2.var= 10
print((c2.real, c2.imag, c2.var))
print(c2.var)

>>>#Cab Booking

class cab:
    def __init__(self,name,km,pickup,drop,fare,nop,cabs):
        self.name=name
        self.km=km
        self.pick=pickup
        self.drop=drop
        self.fare=fare  
        self.nop=nop
        self.cabs=cabs
    def no_of_cabs(self) :
        return self.cabs
    def rate_per_km(self):
        return(self.fare/self.km)
    def avg(self):
        return self.cabs/self.nop
cab1=cab('goodson',40,'HYDBD','DELHI',200,3,10)
print('Rate per km:',cab1.rate_per_km(),'Rs.')
print('Available no: of cabs:',cab1.no_of_cabs())
print('Average:',cab1.avg(),'per passenger.')

>>>#Digital Speedometer

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
            print("breaking speed:",x)  
c1=car(2014,58,60)
print('year ',c1.year)
print('mph ',c1.mph)
print('speed ',c1.speed)
c1.accelerate(10)
c1.brake(120)

>>>#Revenue/Employee (Data Init)

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

>>>#Array

def change(var, list):
    var=1
    list[0]=44
k=3
a=[1,2,3]
change(k, a)
print(k)length=int(input(self.length))
        width=int(input(self.width))
print(a)

>>>#Area and Perimeter (Math)

class rect:
    def __init__(self,length,width):
        
        self.length=length
        self.width=width
    def cal(self):
        return self.length*self.width
    def cal1(self):
        return (2*(self.length+self.width))
c=rect(3,4)
print('area',c.cal())
print('perimeter',c.cal1())

>>>#List1

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
    
>>>#List2

m=['milk','curd','ghee','cream']
c=['candy','toffee','lollipop','chocolate']
d=list['pepsi','mirinda','fanta','coke']
i=input('Enter item:')
if (i==)
    print('Selected',m,' is a diary')
elif (i==c):
    print('Selected',c,'is a sweet')
elif (i==d):
    print('Selected',c,'is a drink')
else:print('item not in list!')

>>> #List operations

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

>>>#Loop

class looping:
        for i in range(1,6):
            print(i,"",i+10,"",i*100,'',i*1000)
l=looping()

>>>#Counter


class counter:
    def __init__(self,x):
        self.x=x
        global l
    def lar(self):
        l=[] 
        for i in range(0,x+1):
            j=[]
            l.append(j)
            return l
    def maximum(self):
        print('The maximum of list is:')
        return max(l)
x=int(input('enter:'))
c=counter(x)
c.lar()
c.maximum()

>>>#Python File Handling

import os
os.chdir('C:\pyf')
a=open('sam1.txt','w+')
for i in range(10):
    a.write("This is a new txt file %d\n\r" %(i+1))
a=open('sam1.txt','r')
x=a.read()
print(x)

>>>#CSV (Excel Sheet)

import csv
import os
os.chdir('C:\pyf')
with open('sample1.csv','r') as File:
    read=csv.reader(File)
    #next(read) #read next line
    for a in File:
        print(a)
        
>>>#.csv

import csv
import os
os.chdir('C:\pyf')
with open('sample1.csv','r+') as f:
    r=csv.reader(f)
    with open('hello.csv','w') as new:
        w=csv.writer(new, delimiter='-')
        for line in r:
            w.writerow(line)
        
>>> For File Handling Topic, create a Folder Naming 'C:\pyf' on Drive! 
>>> Enjoy Coding for Free!
>>> Copyright Protected®
