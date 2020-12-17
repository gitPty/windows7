#!/bin/bash


######kvm虚拟机运行状况，将宿主机pid和vm主机名称联合对应出来

#####create date： 2020/11/2


#####modify date: 2020/11/2



while true
do 

#清空屏幕
    clear
#获得这一时刻的top信息
    top -bn1 >/tmp/kvm_top.txt;
#获得进程号和虚拟机名称对应表
    ps aux|grep -v 'grep'|grep 'qemu-kvm'|awk '{print $2 " "$13}' >/tmp/kvm_list.txt;
#获得top命令前7行，汇总信息行
    cat /tmp/kvm_top.txt|head -n 7;
#将虚拟机名称放到指定信息的一行上，实现名称和监控信息的对应

    for i in `cat /tmp/kvm_list.txt|awk '{print $1}'`;
    do
        grep $i /tmp/kvm_list.txt|awk '{print $2}';
        grep $i /tmp/kvm_top.txt|grep   'qemu-kvm';
    done

#输入相关监控后，暂停10s，以便查看相关数据
    sleep 10
done



