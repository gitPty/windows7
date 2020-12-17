# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 15:07:25 2019

@author: Administrator


注意，在这，想要运行脚本，必须在写完脚本之后再“重新压缩”
一个。zip文件，这样才能识别到密码，原因呢，不晓得，留待以后。


"""
import zipfile
import optparse
from threading import Thread


def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password)
        print("[+] Password= "+password+'\n')
        
    except:
        pass
    
def main():
    parser=optparse.OptionParser("usage%prog "+"-f <zipfile> -d <dictionary>")
    parser.add_option('-f',dest='zname',type='string',
                      help='specify zip file')
    parser.add_option('-d',dest='dname',type='string',
                      help='specify dictionary file')
    
    (options,args)=parser.parse_args()
    if (options.zname==None) or (options.dname==None):
        print(parser.usage)
        exit(0)
    else:
        zname=options.zname
        dname=options.dname
    
    zFile=zipfile.ZipFile(zname)
    passFile=open(dname)
    for line in passFile.readlines():
        password=line.strip('\n')
        t=Thread(target=extractFile,args=(zFile,password))
        t.start()
            
if __name__=='__main__':
    main()
    