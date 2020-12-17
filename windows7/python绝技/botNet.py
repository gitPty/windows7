# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:00:57 2019

@author: Administrator
"""

import optparse 
from pexpect import pxssh


class Client():
    def __init__(self,host,user,password):
        self.host=host
        self.user=user
        self.password=password
        self.session=self.connect()
        
    def connect(self):
        try:
            s=pxssh.pxssh()
            s.login(self.host,self.user,self.password)
            return s
        except Exception as e:
            print(e)
            print('[-] Error Connecting')
            
    def send_command(self,cmd):
        self.session.sendline(cmd)# 发送字符串,等待命令提示符,打印ssh命令的结果.
        self.session.prompt()
        return self.session.before
def botnetCommand(command):
    for client in botNet:
        output=client.send_command(command)
        print('[*] Output from ' +client.host)
        print('[*] '+output+'\n')
        
def addClient(host,user,password):
    client=Client(host,user,password)
    botNet.append(client)
    
botNet=[]
addClient('10.134.196.21','root','Foxconn99')
addClient('10.134.196.22','root','Foxconn99')
botnetCommand('uname -v')
botnetCommand('cat /etc/issue')
