# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:38:25 2019

@author: Administrator
"""

'''
from __future__ import(absolute_import,division,
                       print_function,unicode_literals)
import requests
try:
    #python2.x版本
    from urllib2 import urlopen
except ImportError:
    #python 3.x 版本
    from urllib.request import urlopen
import json


json_url ='https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response =urlopen(json_url)
#读取数据
req =response.read()
#将数据写入文件
with open ('btc_close_2017_urllib.json','wb') as f:
    f.write(req)
    
#加载json模式
file_urllib= json.loads(req)
#print(file_urllib)



json_url ='https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req1 =requests.get(json_url)
#将数据写入文件
with open('btc_close_2017_request.json','w') as f:
    f.write(req1.text)
    
file_requests =req1.json()   
'''
'''
import json
import pygal
import math
from itertools import groupby

def draw_line(x_data,y_data,title,y_legend):
    xy_map=[]
    for x,y in groupby(sorted(zip(x_data,y_data)),key=lambda _: _[0]):     
        #这里的'_'可以使任意字符，只是一种groupby分组方式
        y_list =[v for _,v in y]
        xy_map.append([x,sum(y_list) / len(y_list)])
    x_unique,y_mean =[*zip(*xy_map)]
    line_chart =pygal.Line()
    line_chart.title =title
    line_chart.x_labels =x_unique
    line_chart.add(y_legend,y_mean)
    line_chart.render_to_file(title+'.svg')
    return line_chart

#将数据加载到一个列表中
filename ='btc_close_2017.json'
with open(filename) as f:
    btc_data =json.load(f)

dates=[]
months=[]
weeks=[]
weekdays=[]
closes=[]


    
#打印每一天的信息
for bit_dict in btc_data:
    dates.append(bit_dict['date'])
    months.append(int(bit_dict['month']))
    weeks.append(int(bit_dict['week']))
    weekdays.append(bit_dict['weekday'])
    closes.append(int(float(bit_dict['close'])))


idx_month =dates.index('2017-12-01')
idx_week =dates.index('2017-12-11')
wd=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']


weekdays_int =[wd.index(w)+1 for w in weekdays[1:idx_week]]     #index()返回索引值.


line_chart_weekday =draw_line(weekdays_int,closes[1:idx_week],'收盘星期均值（￥）','星期均值')
line_chart_weekday.x_labels =['周一','周二','周三','周四','周五','周六','周日']
line_chart_weekday.render_to_file('收盘星期均值（￥）.svg')
line_chart_week =draw_line(weeks[1:idx_week],closes[1:idx_week],'收盘周日均值2 （￥）','周日均值')
line_chart_month =draw_line(months[:idx_month],closes[:idx_month],'收盘价月日均值 （￥）','月日均值')
line_chart_month
line_chart_week
line_chart_weekday

    
#print("{}is month {}week{},{},the close price is {}RMB".format(date,month,week,weekday,close))
   
line_chart=pygal.Line(x_label_rotation=20,show_minor_x_labels=False)
line_chart.title='收盘价 (￥)'
line_chart.x_labels =dates
N=20    #x轴每个20天显示一次   ，步进单位
line_chart.x_labels_major=dates[::N]
closes_log=[math.log10(_) for _ in closes]
line_chart.add('收盘价',closes_log)
line_chart.render_to_file('收盘价折线图 (￥)  .svg')
'''






with open('收盘价3Dashboard.html','w',encoding='utf-8') as html_file:
    html_file.write('<html><head><title>收盘价Dashboard</title><meta chartset="utf-8"></head><body>\n')
    for svg in['收盘星期均值（￥）.svg','收盘周日均值2 （￥）.svg','收盘价月日均值 （￥）.svg','收盘价折线图 (￥)  .svg']:
        html_file.write('  <object type="image/svg+xml" data="{0}"\
                        height=500></object>\n'.format(svg))
    html_file.write('</body></html>')