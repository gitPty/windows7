# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:26:21 2019

@author: Administrator
"""

#Keras使用测试,神经网络,sklearn中无神经网络.深度学习本身就是神经网络
from sklearn import datasets
from keras.models import Sequential
from keras.layers.core import Dense,Dropout,Activation
from keras.optimizers import SGD



iris=datasets.load_iris()
model=Sequential()      #模型初始化
model.add(Dense(20))     #添加输入层(20节点),第一隐藏层64节点的链接
model.add(Activation('tanh'))   #第一隐藏层用tanh作为激活函数
model.add(Dropout(0.5))         #使用Dropout防止过拟合
model.add(Dense(64))         #添加第一隐藏层64节点,第二隐藏层64节点的链接
model.add(Activation('tanh'))   #第二隐藏层用tanh作为激活函数
model.add(Dropout(0.5))         #使用Dropout防止过拟合
model.add(Dense(1))          #添加第二隐藏层64节点,输出层1节点的链接
model.add(Activation('sigmoid')) #输出层用sigmoid作为激活函数

sgd=SGD(lr=0.1,decay=1e-6,momentum=0.9,nesterov=True)#定义求解算法
model.compile(loss='mean_squared_error',optimizer=sgd)#编译生成模型,损失函数为
#平均误差平方和

model.fit(iris.data,iris.target,nb_epoch=20,batch_size=16)#训练模型
score=model.evaluate(5.0,3.6,batch_size=16)#测试模型
                     








