#!/bin/bash

#create_date 2020/11/15
#modify_date 2020/11/15

# by pty
#判断是否为root用户
if [ `whoami` != "root" ];then
    echo " only root can run it"
    exit 1
fi


#########

#设置PS 显示，不然太单调了,最后的\$ 要有个转义\\ $ 
echo "PS1='\[\033[01;35m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\\$ '" >> ~/.bashrc
source ~/.bashrc

#设置 http代理
echo "export http_proxy='http://10.134.99.64:66'" >> /etc/profile
echo "export https_proxy='http://10.134.99.64:66'" >> /etc/profile

source /etc/profile

#关闭防火墙和selinux

setenforce 0
sed -i "s/enforcing/disabled/g" /etc/selinux/config

systemctl stop firewalld
systemctl disable firewalld


scp -r root@10.134.196.21:/etc/yum.repos.d/k8s-repos/* /etc/yum.repos.d/


#添加公网DNS
#echo "nameserver 8.8.8.8" >> /etc/resolv.conf
#echo "nameserver 114.114.114.114" >> /etc/resolv.conf

yum clean all && yum makecache fast
#时间同步服务
#yum –y install chrony
#systemctl start chronyd && systemctl enable chronyd
#timedatectl set-timezone Asia/Shanghai && timedatectl set-ntp yes
#timedatectl set-time "11:22:00"

sleep 60
echo "please wait for 60s"
# 重启以应用selinux配置
#reboot





echo "installing docker-ce"
yum -y  install docker-ce
swapoff -a 
systemctl start docker
systemctl enable docker
sleep 30
# 判断是否安装成功
flag=$(systemctl is-active docker)
if [[ "$flag" == "active"  ]]
then 
    echo "installed docker"
else
    echo "inactive,please check"
    exit 1
fi

##########
echo "scp daemon.json ,please input master pass"
#编辑daemon.json ,配置docker加速
mkdir /etc/docker
scp root@10.134.196.21:/etc/docker/daemon.json /etc/docker/daemon.json


##########
#编辑docker专用代理
mkdir -p /etc/systemd/system/docker.service.d
echo '[Service]' >/etc/systemd/system/docker.service.d/https-proxy.conf
echo 'Environment="HTTP_PROXY=http://10.134.99.64:66"' >> /etc/systemd/system/docker.service.d/https-proxy.conf

#重新加载配置文件
echo "sighup for docker"
systemctl daemon-reload
systemctl restart docker



echo "installing k8s compnents"
yum -y install kubelet kubeadm kubectl 
mkdir /root/.kube

# 设置net-bridge。
cat << eof > /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward=1
eof
sysctl -p /etc/sysctl.d/k8s.conf
#加载ipvs模块
source ~/ipvs.modules
#编辑kubelet，忽略swap 和启用ipvs
cat << eof > /etc/sysconfig/kubelet
KUBELET_EXTRA_ARGS="--fail-swap-on=false"
KUBE_PROXY_MODE=ipvs
eof

systemctl restart kubelet
# 开启iptables转发功能
iptables -P FORWARD ACCEPT
#特别注意，使用代理的时候配置代理服务器支持的代理http://, 有的代理服务器没配置https的代理，不要乱用https://

#
scp root@10.134.196.21:/root/.kube/config /root/.kube/config


systemctl enable kubelet 


unset http_proxy
unset https_proxy
echo "join the cluster"
kubeadm join 10.134.196.21:6443 --token agp8v9.4n5zuy4qkwd522nm --discovery-token-ca-cert-hash sha256:e694a59cc9e0665bf5025e9a2aea3f840d217eb9b8df2529c2663be10edc4caf









#####后续加入修改

#报错1 ： 因为没有内网的DNS服务器，
#1. 加入主机hosts文件 或者 启用参数 --kubelet-preferred-address-types=InternalIP,Hostname
#2. 或者编辑kubectl -n kube-system edit cm coredns 的hosts模块，手动添加dns解析

#报错2：x509: certificate signed by unknown authority
#3. vim /var/lib/kubelet/config.yaml 添加最后一行 serverTLSBootstrap: true  之后重启kubelet服务






































