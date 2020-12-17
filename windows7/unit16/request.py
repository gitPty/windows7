# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:02:25 2019

@author: Administrator
#"""
#注意，文件名不要叫requests，与模块名冲突，会报错
#AttributeError: module 'requests' has no attribute 'get'

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS




#执行API 调用并存储响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status code :",r.status_code)

#将API响应存储在一个变量中
response_dict=r.json()
print("Total repositories :",response_dict['total_count'])


#探索有关仓库的信息
repo_dicts=response_dict['items']
print("Repositories returned: ",len(repo_dicts))


names,plot_dicts=[],[]
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
#    stars.append(repo_dict['stargazers_count'])
    plot_dict={
            'value':repo_dict['stargazers_count'],
            'label':str(repo_dict['description']),
            #数据中有一个description的值是null，会报错Nonetype异常，所以要从转换string类型
            'xlink':repo_dict['html_url'],
            }
    plot_dicts.append(plot_dict)
##可视化

#通过修改实例my_config属性来设置图形显示


my_style=LS('#333366',base_style= LCS)

my_config =pygal.Config()


my_config.x_label_rotation=45
my_config.show_legend=False

#设置标题、主标签和副标签
my_config.title_font_size=24
my_config.label_font_size=14
my_config.major_label_font_size =30
#设置较长的项目名缩短为15个字符
my_config.truncate_label=15
#隐藏水平线
my_config.show_y_guides=False

my_config.width=1000


chart =pygal.Bar(my_config,style=my_style)    
chart.title='Most-Starred Python Projects on Github'
chart.x_labels=names
chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
    
##研究第一个仓库
#repo_dict =repo_dicts[0]
#print("\nkeys:",len(repo_dict))
#for key in sorted(repo_dict.keys()):
#    print(key)
#    
    

#处理结果
#print(response_dict.keys())



'''

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style= LS('#333366',base_style=LCS)
chart =pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)

chart.title= 'Python Projects'
chart.x_labels=['httpie','django','flask']

plot_dicts=[{'value':16101,'label':'Description of httpie.'},
            {'value':15028,'label':'Description of django.'},
            {'value':14798,'label':'Description of flask.'},
            ]
chart.add('',plot_dicts)
chart.render_to_file('bar_description.svg')
'''

