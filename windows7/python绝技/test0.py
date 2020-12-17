# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:19:04 2019

@author: Administrator
"""

import nmap 
def findTgts(subNet):
    nmScan=nmap.PortScanner()
    nmScan.scan(subNet,'445')
    tgtHosts=[]
    for host in nmScan.all_hosts():
        if nmScan[host].has_tcp(445):
            state=nmScan[host]['tcp'][445]['state']
            if state =='open':
            print('[+] Found Target Host: '+host)
            tgtHosts.append(host)
    return tgtHosts
