# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:51:04 2019




注意，在这，想要运行脚本，必须在写完脚本之后再“重新压缩”
一个。zip文件，这样才能识别到密码，原因呢，不晓得，留待以后。


@author: Administrator
"""

import zipfile 
from threading import Thread




def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password)
        print('[+] Found password '+password+'\n')
    except:
        pass
    
def main():
    zFile=zipfile.ZipFile('evil.zip')
    passFile=open('dictionary.txt')
    for line in passFile.readlines():
        password=line.strip('\n')
        t=Thread(target=extractFile,args=(zFile,password))
        t.start()

if __name__=='__main__':
    main()
    