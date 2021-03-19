#2D

import numpy as np
x=np.arange(2,10).reshape(2,4) #(2,4)->(2*4) # Elements in 'arange'.
print(x)

#3D

import numpy as np
y=np.arange(24).reshape(4,3,2)
print(y)

#Append

import numpy as np
x=np.array([[10,20,30],[100,110,120]])
print('Array:',x)
x=np.append(x,[[40,60,50],[90,80,70]])
print("Append Array x:",x)
y=np.sort(x, axis=0)
print("Sort on first axis:",y)
i=np.argsort(x)
print("Indices of x:",i)

#Matrix product of two arrays.

import numpy as np
x = [[1, 0], [1, 1]]
y = [[3, 1], [2, 2]]
print("Matrices and vectors.")
print("x:",x)
print("y:",y)
print("Matrix product of x, y:",'\n',np.matmul(x, y))

#histogram(in plot window)

import numpy as np
import matplotlib.pyplot as plt
nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = np.array([0, 1, 2, 3])
print("nums: ",nums)
print("bins: ",bins)
print("Result:", np.histogram(nums, bins))
plt.hist(nums, bins=bins)
plt.show()

#date and time

import numpy as np
print("Number of weekdays in March 2021:")
print(np.busday_count('2021-03', '2021-04'))
#time and date in array
import numpy as np
import datetime
start = datetime.datetime(2021, 1, 1)
dt_array = np.array([start + datetime.timedelta(hours=i) for i in range(24)])
print(dt_array)

#timestamp

import numpy as np
from datetime import datetime
dt = datetime.utcnow()
print("Current date:")
print(dt)
dt64 = np.datetime64(dt)
ts = (dt64 - np.datetime64('1970-01-01T00:00:00Z')) / np.timedelta64(1, 's')
print("Timestamp:")
print(ts)
print("UTC from Timestamp:")
print(datetime.utcfromtimestamp(ts))

#Scipy

import numpy as np
print(sum(range(4),-1))
#scipy using seaborn
from scipy.stats import norm
import seaborn as sns
data_normal = norm.rvs(size=10000,loc=0,scale=1)
print(data_normal)
# settings for seaborn plotting style
ax = sns.distplot(data_normal,bins=100,kde=True,color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')

>>>Try these exercises with ''' <-Backspace<<<

import numpy as n
'''#common import 
x=n.zeros(5)
print(type(x))
z=n.arange(10,50).reshape(5,8)
print(z)
'''
'''-1
i=n.eye(3)
print(i)
'''
'''0
y=n.random.random((10,10))
print(y)
a=n.matrix(5,dtype=int)
A=a.T()
print(A)
'''
'''1
b=[1,2,0,0,4,0]
arr=n.array(b)
print(arr)
x=n.nonzero(arr)
y=n.zeros(b)
print("indeces of non zero:",x,y)
'''
'''2
y=n.random.mtrand.random((10,3))
ymax,ymin=y.max(),y.min()
print(y,'\n max:',ymax,'\n min:',ymin)
'''
'''3
z=n.ones((4,4))
z[1:-1,1:-1]=0
print(z)
'''
'''4
z=n.zeros(100)
print(z)
'''
'''5
x=n.diag(1+n.arange(4),k=1)
print(x)
'''
'''6,7
z=n.tile(([0,1],[1,0]),(8,8))
print(z)
'''
