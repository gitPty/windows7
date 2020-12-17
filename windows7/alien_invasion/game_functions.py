# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:53:34 2019

@author: Administrator
"""

import sys

import pygame
from bullet import Bullet
from alien import Alien
from time import sleep





def check_keydown_events(event,ai_settings,screen,ship,bullets):
    '''響應按鍵'''
    if event.key == pygame.K_RIGHT:
        #向右移動飛船
        ship.moving_right=True
    elif event.key ==pygame.K_LEFT:
        ship.moving_left =True        
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()
        
def fire_bullet(ai_settings,screen,ship,bullets):
    '''如果还没有达到限制，就再新建一个子弹对象'''
    if len(bullets) < ai_settings.bullets_allowed:
        #创建一颗子弹。，并将其加入到编组，bullets中
        new_bullet =Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)
    
        

def check_keyup_events(event,ship):
    '''響應鬆開'''
    if event.key== pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key ==pygame.K_LEFT:
        ship.moving_left =False    
        
def check_events(ai_settings,screen,stats,play_button,ship,aliens,
                 bullets):
    #響應按鍵和鼠標事件
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
            
        
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y =pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,play_button,ship,
                              aliens,bullets,mouse_x,mouse_y)
            
            
            
def check_play_button(ai_settings,screen,stats,play_button,ship,aliens,
                      bullets,mouse_x,mouse_y):
    '''在玩家单机play按钮后开始新游戏'''
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #隐藏光标
        pygame.mouse.set_visible(False)
        
        
        #重置游戏统计信息
        stats.reset_stats()
        stats.game_active =True
        

        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()


        #创建一群新的外星人，并让飞船居中
        create_fleet(ai_settings,screen,ship,aliens)        
        ship.center_ship()
        
            
            
def update_screen(ai_settings,screen,stats,ship,aliens,bullets,
                  play_button):
    #更新屏幕圖像，並切換到新屏幕
    
    
    #每次循環都會重繪屏幕
    screen.fill(ai_settings.bg_color)
    
    #下飞船和外星人后面重新绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    aliens.draw(screen)
    
    #如果游戏处于非活动状态，就绘制play按钮
    if not stats.game_active:
        play_button.draw_button()
    
    #讓最近繪製的屏幕可見
    pygame.display.flip()


def get_number_aliens_x(ai_settings,alien_width):
    '''计算每行可容纳多少外星人'''
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2* alien_width))
    return number_aliens_x


def get_number_rows(ai_settings,ship_height,alien_height):
    '''计算屏幕可容纳多少人'''
    #初始设置外星人纵向间距为其高度
    available_space_y = (ai_settings.screen_height - 
                         (3* alien_height) - ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows
    





def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    '''创建一个外星人并将其放在当前行'''
    
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x =alien_width + 2* alien_width* alien_number
    alien.rect.x =alien.x
    alien.rect.y = alien.rect.height + 2* alien.rect.height *row_number
    aliens.add(alien)






    
def create_fleet(ai_settings,screen,ship,aliens):
    '''创建外星人群'''
    #创建一个外星人，并确认一行可容纳多少个外星人
    #外星人间距为外星人宽度
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,
                                  alien.rect.height)
    
    
    #创建外星人群
    for row_number in range(number_rows):
        
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
        
 
    
    
    
    
    
def update_bullets(ai_settings,screen,ship,aliens,bullets):
    '''跟新子弹位置，并'''
    bullets.update()
    
    #删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
         #print(len(bullets))
         
         
         
    check_bullet_alien_collision(ai_settings,screen,ship,aliens,bullets)
    
    
    
def check_bullet_alien_collision(ai_settings,screen,ship,aliens,bullets):
    '''检查子弹和外星人的碰撞'''
    #检查是否有子弹集中了外星人
    #如果是这样，就删除相应的子弹和外星人
    collisions =  pygame.sprite.groupcollide(bullets,aliens,True,True)
         
    
    if len(aliens)==0:
        #删除现有的子弹并新建一群外星人
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
 


def check_fleet_edges(ai_settings,aliens):
    '''如果有外星人到达边缘时候，采取相应措施'''
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
        
        
def change_fleet_direction(ai_settings,aliens):
    '''将整群外星人下移动，并改变他们的方向'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1




def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    '''响应被外星人撞到的飞船'''
    if stats.ships_left >0:
        #将ships_left减一
        stats.ships_left -= 1
    
        #清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
    
        #创建一群新的我爱学那个人，并将飞船放到屏幕中央
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship
    
        #暂停
        sleep(0.5)  
    
    else:
        stats.game_active =False
        pygame.mouse.set_visible(True)
   
    

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    '''检查是否有外星人到达屏幕底端'''
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #想飞船被撞倒一样进行处理
            ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
            break

        
         
def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    '''更新外星人群组中所有外星人的位置'''
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    
    
    #检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
        
        
    #检查是否有外星人到达屏幕底端
    check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)
        
        
        

        
        
        

        
        
        
        
        
        
        
        
        
        
        
        