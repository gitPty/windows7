#/bin/bash

#create_date 2020/11/9

#modify_date 2020/11/9

# 修改虚拟机名称的脚本

#old_name=$1
#new_name=$2
#定义脚本参数个数
ARGS=2
#如果参数不等于2 ，打印脚本的使用方法信息
if [ $# -ne "$ARGS" ]
then
    #打印脚本的使用方法到标准输出
    echo "Usage: `basename $0` old_name new_name"
    exit 2
fi

state=`virsh list --all | grep $1 | awk '{print $NF}' `
names=`virsh list --all | awk '{print $2}'| tail -n +2 `
#虚拟机先关机，然后检查状态。

#检查输入的名称是否有效，$1旧名称是否在列表中，$2新名称是否不在列表中
result1=$(echo $names| grep "$1")
result2=$(echo $names|grep "$2")
if [[ "$result1" != "" ]];then
    echo "old_name check ok"
    if [[ "$result2" == ""  ]]
    then
        echo "new_name check ok"
    else
        echo " new_name has already exists"
        exit 1
    fi
else
    echo "invalid old_name"
    exit 1
fi


echo "check if  shudown $1"
# 检查是否已关机，如果没有再等60s
if [[ "$state" != "off" ]]
then
    echo "$1 not shutdown,please wait "
    virsh shutdown $1
    sleep 90s
else
    echo "check shutdown OK~"
fi



echo "changing the xml  configuration ."
#定义：virsh definexxx.xml xxx为xml文件所在的路径及文件名称，在当前目录下则不写路径

#启动：virsh start xyz xyz为虚拟机xml配置文件中虚拟机的名字<name>rhel6.2_2</name>

#停止：virsh shutdownxyz 此方法为正常关机方法，需要一段才能关机

#下电：virsh destroy xyz 此方法为暴力下电，虚拟机立即关闭^H

#检查虚拟机状态是否为shutdown

virsh dumpxml $1  > /etc/libvirt/qemu/$2.xml
#修改xml文件中的名字,这里要注意硬盘名字一定要用主机名 。
###注意注意。
sed -i "s/$1/$2/g" /etc/libvirt/qemu/$2.xml
#删除uuid的一行，重启后会自动生成
sed -i 's/<uuid>.*//' /etc/libvirt/qemu/$2.xml

#修改硬盘名称，命名太乱了 ，这里太复杂了，不改了先。
echo "changing disk name"
cd /vmdisk


file=$(ls |grep  "$1" )
##这里注意单引号和双引号的区别，“” 可以解析$1，$2变量，‘’ 是纯字符输出
for f in $file
do 
    new_disk_name=`echo $f|sed "s/$1/$2/g"`
    mv $f $new_disk_name
done

echo "disk name changed !"


















#删除 old命名的虚拟机
virsh undefine $1 
#新建虚拟机
virsh define  /etc/libvirt/qemu/$2.xml

#开启虚拟机 并加入autostart组。
virsh start $2
virsh autostart $2


echo "autostart $2"
echo "starting  $2"
