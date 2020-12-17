# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 09:23:02 2019

@author: Administrator
"""

import ftplib
def returnDefault(ftp):
    try:
        dirList=ftp.nlst()
    except:
        dirList=[]
        print("[-] Could not list dictionary contents.")
        print('[-] Skipping To Next Target.')
        return
    retList=[]
    for fileName in dirList:
        fn=fileName.lower()
        if('.php' in fn) or('.htm' in fn) or ('.asp' in fn):
            print('[+] Found default page: '+fileName)
            retList.append(fileName)
    return retList
host='10.134.196.21'
userName='test01'
passWord='1'
ftp=ftplib.FTP(host)
ftp.login(userName,passWord)
returnDefault(ftp)