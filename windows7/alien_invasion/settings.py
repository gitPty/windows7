# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:27:01 2019

@author: Administrator
"""

class Settings():
    #存儲《外星人入侵》的所有設置的類
    #屏幕設置
    def __init__(self):
        
        self.screen_width = 1200
        self.screen_height =800
        self.bg_color =(230,230,230)
        
        #飛船設置,#飛船移動速度1.5個像素
        self.ship_speed_factor = 1.5 
        self.ship_limit =3
        
        
        
        #子弹设置
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed =30
        
        #外星人设置
        self.alien_speed_factor =1
        self.fleet_drop_speed = 10
        #fleet_direction为1，表示向右移动，为-1表示向左移动
        self.fleet_direction =1
        
        
    