ansible node -m copy -a "src=/etc/yum.repos.d/docker-ce.repo dest=/etc/yum.repos.d/docker-ce.repo"
ansible node -m copy -a "src=/etc/yum.repos.d/kubernetes.repo dest=/etc/yum.repos.d/kubernetes.repo"
ansible node -m copy -a "src=/etc/yum.repos.d/epel.repo dest=/etc/yum.repos.d/epel.repo"

ansible node -m shell -a "yum clean all && yum makecache"
