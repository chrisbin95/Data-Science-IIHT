#Cntrl+C #Cntrl+V #PYCODING

#1

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
import numpy as np
brics = pd.DataFrame(dict)
print(brics)

#2

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

#3

import pandas as pd
import numpy as np
dates = pd.date_range("20210101", periods=12)
print(dates)
df = pd.DataFrame(np.random.randn(12, 4), index=dates, columns=list("ABCD"))
print(df)

#4

dict={"Name":["Arun","Shiva","Ram","Anpu"],"ID":["id021","id043","id090","id082"],
      "Salary":[20000,3000,5000,7000],"Location":["JayaNgr","Huli","Coim","busavan"]}
