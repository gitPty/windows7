#!/bin/bash
#此次主要使用了10.148.53.235的本地yum更新仓库,使用wget或者curl -O 选项(大o非0)

#如果本机有外网代理设置,要先关闭,unset env中的proxy就行了.


PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH


#进入repo目录并下载本地源的repo文件
cd /etc/yum.repos.d/
mv CentOS-Base.repo CentOS-Base.repo.bak
wget http://10.148.53.235/script/CentOS-Base.repo -P /etc/yum.repos.d/

#判断是否正确下载了53.235的repo文件

filename=/etc/yum.repos.d/CentOS-Base.repo
if [ ! -f "${filename}" ];then
	echo "local yum repo  download failed!"
	exit 1
	
else 
	yum clean all
	yum makecache
	echo "configration successful!"
	echo "验证是否成功,yum一下"
	




	yum install mlocate

fi


