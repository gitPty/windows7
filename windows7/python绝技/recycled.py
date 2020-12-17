# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 11:18:41 2019

@author: Administrator
"""

#用脚本寻找被删除到回收站的数据.
#回收站的目录为c:\Recycled\
import optparse
from winreg import *
import os 

#windows不通版本的回收站名称.win7是最后一个string
def returnDir():
    dirs=['C:\\Recycled\\','C:\\Recycler\\','C:\\$Recycle.Bin\\' ]
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None

 #将SID的值转换为具体用户名
def sid2user(sid):
    try:
        key=OpenKey(HKEY_LOCAL_MACHINE,"SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"
                    +'\\'+sid)
        (value,type)=QueryValueEx(key,'ProfileImagePath')
        user=value.split('\\')[-1]
        return user
    except:
        return sid

#查找各个用户名下的回收站文件.
def findRecycled(recycleDir):
    dirList=os.listdir(recycleDir)
    for sid in dirList:
        files=os.listdir(recycleDir+sid)
        user=sid2user(sid)      #将SID的值转换为具体用户名
        print('\n[*] Listing Files For USer: '+str(user))
        for file in files:
            print('[+] Found File: '+str(file))
def main():
    recycledDir=returnDir()     #实例化
    findRecycled(recycledDir)
if __name__=='__main__':
    main()
    