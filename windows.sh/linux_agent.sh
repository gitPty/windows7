#!/bin/bash

centos_agent(){
    scp @10.122.40.91:/root/zabbix_agents.tar.gz /usr/local \
    && echo "Copy success !"
    sed -i "7s?^SELINUX.*?SELINUX=disabled?g" /etc/selinux/config \
    && chk=`cat /etc/selinux/config | grep SELINUX=disabled`
    if [ "$chk" == "SELINUX=disabled" ]; then
        systemctl stop firewalld.service && systemctl disable firewalld.service
        chkfw=`systemctl is-active firewalld`
        if [ "$chkfw" == "unknown" ]; then
	    cd /usr/local/ && mkdir zabbix_agentd && tar -xzf zabbix_agents.tar.gz -C ./zabbix_agentd \
            && rm -rf /usr/local/zabbix_agents.tar.gz && cd zabbix_agentd
        else
            echo "$chkfw" != "unknown"
        fi
    fi
                  
    host=Hostname=`hostname`
    sed -i "s?LogFile=/tmp/zabbix_agentd.log?LogFile=/var/log/zabbix_agentd/zabbix_agentd.log?g" /usr/local/zabbix_agentd/conf/zabbix_agentd.conf \
    && sed -i "s?Server=127.0.0.1?Server=10.122.40.91?g" /usr/local/zabbix_agentd/conf/zabbix_agentd.conf \
    && sed -i "s?ServerActive=127.0.0.1?ServerActive=10.122.40.91?g" /usr/local/zabbix_agentd/conf/zabbix_agentd.conf \
    && sed -i "s?Hostname=Zabbix server?"$host"?g" /usr/local/zabbix_agentd/conf/zabbix_agentd.conf \
    && useradd -M zabbix -s /sbin/nologin && chown zabbix:zabbix /usr/local/zabbix_agentd/sbin/zabbix_agentd \
    && mkdir /var/log/zabbix_agentd && cd /var/log/ && chown -R zabbix:zabbix zabbix_agentd/ \
    && /usr/local/zabbix_agentd/sbin/zabbix_agentd -c /usr/local/zabbix_agentd/conf/zabbix_agentd.conf \
    && echo "/usr/local/zabbix_agentd/sbin/zabbix_agentd -c /usr/local/zabbix_agentd/conf/zabbix_agentd.conf" >> /etc/rc.d/rc.local \
    && chmod +x /etc/rc.d/rc.local 
    chkport=`netstat -nltup | awk 'NR>2{print $4}' | grep ":10050"`
    if [ "$chkport" != "" ]; then
        echo "zabbix_agentd the service is running !"
    else
        echo "zabbix_agentd the service is not running !"
    fi
                 }

ubuntu_agent(){
    scp @10.122.40.91:/root/zabbix_agents.tar.gz /usr/local && ufw disable
    chkfw=`ufw status |awk 'NR=1{print $2}' |grep "inactive"`
    if [ "$chkfw" = "inactive" ];then
        cd /usr/local/ && mkdir zabbix_agentd && tar -xzf zabbix_agents.tar.gz -C ./zabbix_agentd \
        && rm -rf /usr/local/zabbix_agents.tar.gz && cd zabbix_agentd
    else
        echo "$chkfw" != "inactive"
    fi

    host=Hostname=`hostname`
    sed -i "s?LogFile=/tmp/zabbix_agentd.log?LogFile=/var/log/zabbix_agentd/zabbix_agentd.log?g" /usr/local/zabbix_agentd/conf/zabbix_agentd.conf \
    && sed -i "s?Server=127.0.0.1?Server=10.122.40.91?g" /usr/local/zabbix_agentd/conf/zabbix_agentd.conf \
    && sed -i "s?ServerActive=127.0.0.1?ServerActive=10.122.40.91?g" /usr/local/zabbix_agentd/conf/zabbix_agentd.conf \
    && sed -i "s?Hostname=Zabbix server?"$host"?g" /usr/local/zabbix_agentd/conf/zabbix_agentd.conf \
    && useradd -M zabbix -s /sbin/nologin && chown zabbix:zabbix /usr/local/zabbix_agentd/sbin/zabbix_agentd \
    && mkdir /var/log/zabbix_agentd && cd /var/log/ && chown -R zabbix:zabbix zabbix_agentd/ \
    && /usr/local/zabbix_agentd/sbin/zabbix_agentd -c /usr/local/zabbix_agentd/conf/zabbix_agentd.conf \
    && echo "/usr/local/zabbix_agentd/sbin/zabbix_agentd -c /usr/local/zabbix_agentd/conf/zabbix_agentd.conf" >> /etc/rc.d/rc.local \
    && chmod +x /etc/rc.d/rc.local
    chkport=`netstat -nltup | awk 'NR>2{print $4}' | grep ":10050"`
    if [ "$chkport" != "" ]; then
        echo "zabbix_agentd the service is running !"
    else
        echo "zabbix_agentd the service is not running !"
    fi
                 }

chkos=`hostnamectl | awk 'NR=7{print $3}' |grep "CentOS"`
if [ "$chkos" = "CentOS" ]; then
    echo "Centos zabbix is being installed"
    centos_agent
else
    echo "Ubuntu zabbix is being installed"
    ubuntu_agent
fi
