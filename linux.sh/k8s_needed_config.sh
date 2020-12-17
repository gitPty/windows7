# 设置net-bridge。
cat << eof > /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
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

