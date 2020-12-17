@echo off
color fd
cd \
::IP from Zabbix Server or proxy where data should be send to.
Set zabbix_server_ip=10.150.7.55
echo Creating zabbix install dir
mkdir c:\zabbix
echo Copying Zabbix install file
net use \\10.134.99.129 "Enterprise@2019**" /user:"foxera\admin"
if %processor_architecture% EQU x86 xcopy \\10.134.99.129\PDSSshare\Software\zabbix_agents\win86 c:\zabbix /s
if %processor_architecture% EQU AMD64 xcopy \\10.134.99.129\PDSSshare\Software\zabbix_agents\win64 c:\zabbix /s
echo Modiy zabbix configuration files
echo LogFile=c:\zabbix\bin\zabbix_agentd.log >> C:\zabbix\conf\zabbix_agentd.win.conf
echo Server=%zabbix_server_ip% >> C:\zabbix\conf\zabbix_agentd.win.conf
echo ServerActive=%zabbix_server_ip% >> C:\zabbix\conf\zabbix_agentd.win.conf
echo Hostname=%COMPUTERNAME% >> C:\zabbix\conf\zabbix_agentd.win.conf
echo start zabbix servic
C:\zabbix\bin\zabbix_agentd.exe -i -c C:\zabbix\conf\zabbix_agentd.win.conf
C:\zabbix\bin\zabbix_agentd.exe -s -c C:\zabbix\conf\zabbix_agentd.win.conf 
echo start zabbix services
net start "Zabbix Agent"
echo set zabbix service auto
sc config "Zabbix Agent" start= auto
echo Zabbix agentd Configuration and Install Successful
