# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 17:24:25 2019

@author: Administrator
"""

import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """針對目標類的測試"""
    def setUp(self):
         #創建一個對象和一組答案以供測試
         question ="What language did you first learn to speak?"
         self.my_survey=AnonymousSurvey(question)
         self.responses=['english','spanish','mandarin']
         
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)
    
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)#store對於列表來說可以用append來實現
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
            
"""    
    def test_store_single_response(self):
       #測試單個答案的保存狀況
        question ="What language did you first learn to speak?"
        my_survey=AnonymousSurvey(question)
        my_survey.store_response('nihong')
        
        self.assertIn('nihong',my_survey.responses)
    
    def test_store_three_responses(self):
        #"測試三個人的答案保存"
        question ="What language did you first learn to speak?"
        my_survey=AnonymousSurvey(question)
        responses=['english','spanish','mandarin']
        for response in responses:
            my_survey.store_response(response)
            
        for response in responses:
            self.assertIn(response,my_survey.responses)
"""
     
         
unittest.main()
