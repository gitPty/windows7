# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:16:56 2019

@author: Administrator
"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk


while True:
    
    #创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw =RandomWalk(50000)
    rw.fill_walk()
    
    
    #调整绘图窗口尺寸
    plt.figure(dpi=128,figsize=(3,1))
    #单位是英寸,一英寸等于2.54厘米
    point_numbers =list(range(rw.num_points))
    
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,
                edgecolor='none',s=1)
    
    #突出起点和终点
    plt.scatter(0,0,c='green',edgecolor ='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor ='none',s=100)
    
    
    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running =input("Make another walk?(y/n):")
    if keep_running =='n':
        break