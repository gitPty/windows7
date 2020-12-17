# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:14:04 2019

@author: Administrator
"""

import csv
from datetime import datetime

from matplotlib import pyplot as plt

#从文件中获取最高气温
filename ='death_valley_2014.csv'
with open (filename) as f:
    reader =csv.reader(f)
    header_row =next(reader)
   
    
    dates,highs,lows=[],[],[]
    for row in reader:
        try:
            current_date =datetime.strptime(row[0],"%Y-%m-%d")
            high=int(row[1])
            low =int(row[3])
        except ValueError:
            print(current_date,"missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        
        
    #print(highs)
    
#根据数据绘制图像
    
fig =plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.3)

#设置图像格式
plt.title("Daily high and low tempratures - 2014-death",fontsize =24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temprature (F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=10)
plt.xlim(dates[0],dates[-1])

plt.show()