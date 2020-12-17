#!/bin/bash

#create_date 2020/11/15
#modify_date 2020/11/15

# $name=$1 第一个参数传入要定义的dom名称
# $2 指定OS版本，所以在xml文件目录下要新建模板xml文件，如windows2016.xml,centos7.6.xml,rhel7.6.xml
# $2 = windows2012,$2=windows2016 ...
# names 变量代表dom名称，names代表 xml文件的去掉xml后缀后名称，主要是检查模板名字是否存在
names=`virsh list --all | awk '{print $2}'| tail -n +2 `
names2=`basename -s .xml $(ls /etc/libvirt/qemu|grep .xml$)`
#定义脚本参数个数
ARGS=2
#如果参数不等于2 ，打印脚本的使用方法信息
if [ $# -ne "$ARGS" ]
then
    #打印脚本的使用方法到标准输出
    echo "Usage: `basename $0` CREATE_VM_NAME XML_TEMPLATE_NAME"
    exit 2
fi



echo "==============="
echo "checking input if valid"

#检查输入的名称是否有效，$1旧名称是否 不在virsh列表中，新建的名字不能冲突，$2模板名称是否存在，不能不存在啊。
result1=$(echo $names| grep "$1")
result2=$(echo $names2|grep "$2")
if [[ "$result2" != "" ]];then
    echo "xml_template_name check ok"
    if [[ "$result1" == ""  ]]
    then
        echo "create_name check ok"
    else
        echo " create_name has already exists"
        exit 1
    fi
else
    echo "no this xml_template_name"
    exit 1
fi
echo "==============="


echo "check disk name if valid"
disk_name=$(ls /vmdisk|grep $1)
if [[ "$disk_name" != "" ]]
then
    echo  "disk_name has already exists"
    exit 3
else
    echo "you can use this name: $1_c.img"
fi



echo "==============="

echo "Createing disk NAME_C.img"
echo "Please wait for a few second!"
sleep 10
#创建硬盘文件,raw or qcow2 ,先给个100G 的C盘，后续的盘符使用扩容脚本# 创建模板时指定disk为windows2012_c.img.
qemu-img create -f qcow2 /vmdisk/$1_c.img 100G

echo "disk has been created, type: qcow2,cpa: 100G"
##指定要建立的OS版本，如2012,那么拷贝windows2012 的配置文件
cp /etc/libvirt/qemu/$2.xml /etc/libvirt/qemu/$1.xml

#不需要处理uuid，模板已处理好，只需更改名称，和指定iso文件及磁盘文件即可，mac地址也没有，毕竟是模板。制作模板要考虑到。
#模板就是4 vcpu 和8GiB mem。
#只替换第一次匹配的domain名称,文件中出现的第一次匹配
#参考网页， https://www.cnblogs.com/wjlv/p/10772888.html  这个说的是一行中的第几个匹配
#参考网页： https://www.cnblogs.com/zengjfgit/p/6188311.html    这个是整个文件中的第几个匹配。
# sed -i "0,/$2/s/$2/$1/g" /etc/libvirt/qemu/$1.xml

sed -i "s/$2/$1/g" /etc/libvirt/qemu/$1.xml
#同时替换了domname 和diskname。
echo "==============="
# 模板制作的时候直接指明iso文件 ，并且注意不要被替换。

# 启动机器 
echo "ready to start"
virsh define /etc/libvirt/qemu/$1.xml
virsh start $1
virsh autostart $1
echo "autostart $1"
echo "please login webmanager and vnc this new_vm to install the OS!"




