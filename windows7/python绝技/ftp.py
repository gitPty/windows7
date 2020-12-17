# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 09:45:47 2019

@author: Administrator
"""

import ftplib
def anonLogin(hostname):
    try:
        ftp=ftplib.FTP(hostname)
        ftp.login('anonymous','me@your.com')
        print('\n[*] '+str(hostname) +' FTP Anonymous Logon Succeed.')
        ftp.quit()
        return True
    except Exception as e:
        print('\n[-] '+str(hostname)+' FTP Anonymous Logon Failed .')
        return False
host='10.134.196.21'
anonLogin(host)