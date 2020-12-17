# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:56:28 2019

@author: Administrator
"""

import pygame

class Ship():
    
    
    def __init__(self,ai_settings,screen):
        #初始換飛船並設置其初始位置
        self.screen = screen
        self.ai_settings =ai_settings
        
        #加載飛船圖形並獲取其外接矩形
        self.image=pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect=screen.get_rect()
        
        
        #將每艘新飛船放在屏幕底部中央
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        
        
        #在飛船屬性centerx中存儲小數值
        self.center = float(self.rect.centerx)
        
        #移動標誌位
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        #根據移動標誌調整飛船位置
        #更新center值，而不是rect
        '''這裡出現了個小失誤，前面賦值給center後，忘記將變量更改為center了，
        還思考了很久，很無聊，浪費時間，下午盡量不要編程'''
        if self.moving_right and self.rect.right < self.screen_rect.right:  #保證左右移動不超過邊界。
            self.center +=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -=self.ai_settings.ship_speed_factor
            
            
        #根據self.center更新rect對象
        self.rect.centerx = self.center 
        
    def blitme(self):
        #在指定位置 繪製飛船
        self.screen.blit(self.image,self.rect)
        
        
        
        
        
        
        
        
    def center_ship(self):
        '''让飞船在屏幕居中'''
        self.center = self.screen_rect.centerx