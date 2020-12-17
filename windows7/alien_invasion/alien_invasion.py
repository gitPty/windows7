# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:39:30 2019

@author: Administrator
"""

 
import pygame


from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button







def run_game():
     #初始換遊戲並建立一個屏幕輸出
     pygame.init()
     ai_settings=Settings()
     screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
     pygame.display.set_caption("Alien Invasion")
     
     
     
     #创建paly按钮
     play_button = Button(ai_settings,screen,"Play")
     
     #创建一个用于存储游戏统计信息的实例
     stats = GameStats(ai_settings)
     
     
     
     '''创建一艘飞船，一个子弹编组，一个外星人编组'''
     
     #創建一艘飛船
     ship=Ship(ai_settings,screen)
     
     #创建一个用于存储子弹的编组
     bullets =Group()
     
     aliens = Group()
     #创建外星人群
     gf.create_fleet(ai_settings,screen,ship,aliens)
     
    
     
     #開始遊戲主循環
     while True:
         
         
        
         #見識鍵盤和鼠標事件
         gf.check_events(ai_settings,screen,stats,play_button,ship,
                         aliens,bullets)
         
         if stats.game_active:
             ship.update()
             gf.update_bullets(ai_settings,screen,ship,aliens,bullets)   
             gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
             
             
         #每次循環都會重新繪製屏幕 #讓最近繪製的屏幕可見
         gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,
                          play_button)
         
         
         
         
        
         
        
        
        
run_game() 
