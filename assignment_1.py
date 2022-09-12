# -*- coding: utf-8 -*-
"""Assignment_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bE3OuvqsAxuodQyTTRY2qcxrNQLmZZOK

# Basic Python
"""

from google.colab import drive
drive.mount('/content/drive')



"""## 1. Split this string"""

s = "Hi there Sam!"

s="Hi there Sam!"
print(s.split())

"""## 2. Use .format() to print the following string. 

### Output should be: The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742

planet = "Earth"
diameter = 12742
print( 'The diameter of {} is {} kilometers.' .format(planet,diameter));

"""## 3. In this nest dictionary grab the word "hello"
"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

In[14]
d['k1'][3]['tricky'][3]['target'][3]

"""# Numpy"""

import numpy as np

"""## 4.1 Create an array of 10 zeros? 
## 4.2 Create an array of 10 fives?
"""

import numpy as np
array=np.zeros(10)
print("An array of 10 zeros:")
print(array)
array=np.ones(10)*5
print("An array of 10 fives:")
print(array)

"""## 5. Create an array of all the even integers from 20 to 35"""

import numpy as np
array=np.arange(30,71,2)
print("Array of all the even integers from 30 to 70")
print(array)

"""## 6. Create a 3x3 matrix with values ranging from 0 to 8"""

import numpy as np
x=np.arange(2,11).reshape(3,3)
print(x)

"""## 7. Concatenate a and b 
## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
"""

a=np.array([1,2,3])
b=np.array([4,5,6])
np.concatenate((a,b),axis=0)
np.concatenate((a,b.T),axis=0)
np.concatenate((a,b),axis=None)

"""# Pandas

## 8. Create a dataframe with 3 rows and 2 columns
"""

import pandas as pd
data=[['tom',10],['nick',15],['juli',14]]
df=pd.DataFrame(data,columns=['Name','Age'])
df

"""## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023"""

import datetime
daydelta=datetime.timedelta(days=1)
startdate=datetime.date.today()
enddate=startdate+41*daydelta
for i in range((enddate-startdate).days):
  print(startdate+i*daydelta)

"""## 10. Create 2D list to DataFrame

lists = [[1, 'aaa', 22],
         [2, 'bbb', 25],
         [3, 'ccc', 24]]

list=[[1,'aaa',22],[2,'bbb',24],[3,'ccc',24]]
print(pd.DataFrame(lists))
"""

import pandas as pandas
lists=[[1,'aaa',22],[2,'bbb',25],[3,'ccc',24]]
df=pd.DataFrame(lists, columns=['Sl.No','Name','Number'])
print(df)