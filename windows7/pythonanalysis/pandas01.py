# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 17:29:30 2019

@author: Administrator
"""

import pandas as pd

s=pd.Series([1,2,3],index=['a','b','c'])
d=pd.DataFrame([[1,2,3],[4,5,6]],columns=['a','b','c'])
d2=pd.DataFrame(s)

d.head()
d.describe()

pd.read_excel('data.xls')
pd.read_csv('data.csv',encoding='utf-8')