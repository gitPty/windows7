#!/bin/bash

#create_date 2020/11/23
#modify_date 2020/11/23

yum install -y nfs-utils
systemctl start nfs-utils
systemctl enable nfs-utils
