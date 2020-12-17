#!/bin/bash
#create_date 2020/11/23

#modify_date 2020/11/23

#安装nfs服务端组件。
yum install -y nfs-common nfs-utils rpcbind

mkdir /nfs && chmod 777 /nfs

chown nfsnobody /nfs
cat > /etc/exports << EOF
/nfs *(rw,no_root_squash,no_all_squash,sync)
EOF

#启动nfs
systemctl start rpcbind && systemctl start nfs-server

#开机自启动

systemctl enable rpcbind && systemctl enable nfs-server
