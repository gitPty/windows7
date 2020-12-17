# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:04:40 2019

@author: Administrator
"""

class AnonymousSurvey():
    """收集匿名用戶調查問卷的答案"""
    def __init__(self,question):
        self.question=question
        self.responses=[]
        
        
    def show_question(self):
        """顯示調查問捲的答案"""
        print(self.question)
        
        
    def store_response(self,new_response):
        """存儲單個問卷"""
        self.responses.append(new_response)    
        
    def show_results(self):
        """顯示收集到的所有表格"""
        print("Survey results:")
        for response in self.responses:
            print('- '+response)

    