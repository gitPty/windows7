# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 19:50:30 2019

@author: Administrator
"""
#本脚本功能!
#在笔记本电脑中运行测试无线网络位置的脚本

from winreg import *  #这里的winreg没有下划线_,python3了


def val2addr(val):
    addr=''
    for ch in val:
        addr +='%02x '% ord(ch)#这里的%02x空格是为了下一句的replace()
    addr=addr.strip(' ').replace(' ',':')[0:17]
    return addr
    
def printNets():
    net=r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged'
    #上面的字符串一定要用r标注或者双斜杠表示
    
    key=OpenKey(HKEY_LOCAL_MACHINE,net)
    print('\n[*] Networks you have joined.')
    for i in range(100):
        try:
            guid=EnumKey(key,i)
            netKey=OpenKey(key,str(guid))
            (n,addr,t)=EnumValue(netKey,5)#这个是网关地址
            (n,name,t)=EnumValue(netKey,4)#这个是网络名
            macAddr=val2addr(addr)
            netName=str(name)
            print('[+] '+netName+' '+macAddr)
            CloseKey(netKey)
        except:
            break
            #continue
        
def main():
    printNets()
    
if __name__=='__main__':
    main()          