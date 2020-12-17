#编辑kubelet配置使用systemd driver，yum安装的默认使用cgroups。因为之前docker.sh中写了daemon。json中的docker 也是systemd了，要统一
#不然就会报错，no such file。。。
sed -i 's#config.yaml#config.yaml --cgroup-driver=systemd#g'   /usr/lib/systemd/system/kubelet.service.d/10-kubeadm.conf
systemctl daemon-reload
systemctl restart kubelet
