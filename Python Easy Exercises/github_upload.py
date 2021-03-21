>>>#Addition of integers

import time
start=time.time()
for i in range(1, 100000):
    s=1
    s+=i
print('Addition of integers from: 1 to',i)
end=time.time()
print(f"runtime is: {end - start} sec.")

>>>#deque 

from collections import deque
items=deque([1,2,3,4,5,6,0])
items.rotate(1)
print(items)

>>>#addition

n=input('Enter number:')
sum1=0
for digit in str(n):
    sum1+=int(digit)
print(sum1)

>>>#Divisors of a number

n=int(input('Enter the no:'))
l=[]
x=[]
for i in range(1, n+1):
        if n%i == 0:
            print('The divisors are:',i)
            l.append(i)
print(l)
x=len(l)
print('The no: of divisors of',n,':',len(l)) 

>>>#Factorial of a number

def recur(n):
    if n==1:
        return n
    else:
        return n*recur(n-1)
num=int(input('Enter no:'))
if num<0:
    print("doesnot exist")
elif num == 0:
    print("fact is 0 is 1")
else:print('the fact of',num,'is',recur(num))

>>>#Divisible by 3 using lambda

print(list(filter(lambda x:x%3==0, range(1, 51))),'are no: divisible by 3.')
    
>>>#Even numbers using lambda function

print(list(filter(lambda x: x%2==0, range(0, 101))),'no: that are even.')

>>>#Lambda map 

i=[1,2,3,4,5,6,7,8,9]
print(list(map(lambda x: x**2 if x%2==0 else x**3,i)))

>>>#Operator multiply

import operator
l=[1,2,3,4,5,6,7,8,9]
print(operator.mul,l)

>>>#Regular Expression Examples:

import re
names='ravi','raghav','raghu','ravip'
p=re.compile('rav[?<=a-z]')
for i in names:
    print(re.match(p,i))

#2

import re
s='When is python class. Everyday!'
p2=re.compile('^W')
print(re.search(p2,s))

#3

import re
names='ravi','raghav','raghu','ravip','raghup'
p=re.compile('ra[^A-Z,a-z]')
for i in names:
    print(re.match(p,i))

>>>#Area of the triangle

a=5
b=6
c=7
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('the area of triangle is: %f'%area

>>>#Multiplication Table

num=int(input('\n Enter the number for table: '))
print('\n The multiplication table of',num ,'is:')
for i in range(1, 11):
    x=num*i
    print(num,'*',i,'=', x)
    
>>>#String Operations

num1=int(input(' Enter the Input 1: '))
num2=int(input(' Enter the Input 2: '))
if num1>num2:
    print('\n Input',num1,'is greater than',num2)
elif num1<num2:
    print('\n Input',num1,'is less than',num2)
else:
    print('\n Input',num1,'equal to',num2)
if num1>0:
    for i in range(2,num1):
        if (num1 % i)==0:
            print('\n',num1,'is not a Prime Number.')
            break
    else:
        print('\n',num1,'is a Prime Number!')
def pali(s):
    return s==s[::-1]
s=str(input('\n Enter String for Palindrome check:'))
res = pali(s)
if res:
    print('\n' ,s,'is a Palindrome!')
else:
    print('\n' ,s,'is Not a Palindrome.')

>>>#Greater than of two

a=input('Enter the number1:')
b=input('Enter the number2:')
c=input('Enter the number3:')
if (a>b) and (b>c):
    print('\n',a,'is greater than',b,'and',c)
elif (b>a) and (b>c):
    print('\n',b,'is greater than',a,'and',c)
else:print('\n',c,'is greater than',a,'and',b)
if(a==c) and (a==b) and (a==c):
    print('\n',a,b,c,'are equal')
elif ((a!=b) and (b!=c)):
    print('\n',a,b,c,'are not equal')
else:
    print('\n',a or b or c,'is greater than',a or b or c)




    
        
    






                    
            
            
