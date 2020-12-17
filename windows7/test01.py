# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:58:27 2019

@author: Administrator
"""

import socket
import winreg


# 使用主机名命名软件安装列表
hostname = socket.gethostname()
file = open(r'C:\Users\Administrator\Desktop\%s.txt' % hostname, 'w')

# 需要遍历的两个注册表
sub_key = [r'SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall',
           r'SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall']

software_name = []

for i in sub_key:
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, i, 0, winreg.KEY_ALL_ACCESS)
    for j in range(0, winreg.QueryInfoKey(key)[0]-1):
        try:
            key_name = winreg.EnumKey(key, j)
            key_path = i + '\\' + key_name
            each_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)
            DisplayName, REG_SZ = winreg.QueryValueEx(each_key, 'DisplayIcon')
            DisplayName = DisplayName.encode('utf-8')
            software_name.append(DisplayName)
        except WindowsError:
            pass

# 去重排序
software_name = list(set(software_name))
software_name = sorted(software_name)


for result in software_name:
    file.write(str(result) + '\n')
file.close()