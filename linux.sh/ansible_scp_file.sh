#!/bin/bash

#create 2020/11/16
# modify 2020/11/16

#ansible派发文件，/etc/docker/daemon.json,
ansible node -m copy -a "src=/etc/docker/daemon.json dest=/etc/docker/daemon.json"

