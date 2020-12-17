
yum  install docker-ce

systemctl start docker
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
