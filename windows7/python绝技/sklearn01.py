# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 08:59:45 2019

@author: Administrator
"""

from sklearn.linear_model import LinearRegression
from sklearn import datasets
from sklearn import svm  

iris=datasets.load_iris()   #加载数据集
print(iris.data.shape)      #查看数据集大小


#model = LinearRegression()

#print(model)



clf=svm.LinearSVC(max_iter=10000)                 #建立线性SVM分类器
clf.fit(iris.data,iris.target)      #用数据训练模型
clf.predict([[5.0,3.6,1.3,0.25]])   #训练模型之后,输入新数据预测
clf.coef_       #查看训练好的模型参数