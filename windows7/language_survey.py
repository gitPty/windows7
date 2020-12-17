# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:11:04 2019

@author: Administrator
"""

from survey import AnonymousSurvey
#定義一個問題，並實例化類對象

question ="What language did you first learn to speak?"
my_survey=AnonymousSurvey(question)


#顯示問題並存儲答案，json
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response=input("Language: ")
    if response=='q':
        break
    my_survey.store_response(response)
    
    
#顯示調查結果
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()