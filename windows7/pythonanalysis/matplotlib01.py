# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 15:57:59 2019

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt
import time

start=time.clock()

x=np.linspace(0,10,1000)
y=np.sin(x)+1
z=np.cos(x**2)+1

plt.figure(figsize=(8,4))
plt.plot(x,y,label='$\sin x+1$',color='red',linewidth=2)

plt.plot(x,z,'b--',label='$\cos x^2+1$')
plt.xlabel('Time(s) ')
plt.ylabel('Volt啥')
plt.title('A  Simple Example')
plt.ylim(0,2.2)
plt.legend()    #显示图例左上角或右下角的函数标识


##解决中文标签无法正常显示的问题
plt.rcParams['font.sans-serif']=['SimHei']
#
##解决保存图像是负号'-'显示为方块的问题
#plt.rcParams['axer.unicode_minus']=False    

plt.show()

elapsed=(time.clock()-start)
print("Time used: ",elapsed)