# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 13:58:12 2019

@author: Administrator
"""
'''
#通用requests库 请求代码框架


import requests


def GetHTMLText(url):
    try:
        kv={'User-Agent':'Mozilla/5.0'}
        r=requests.get(url,headers=kv)
        r.raise_for_status()    #如果状态不是200,返回httperr异常
        r.encoding=r.apparent_encoding
        return r.text
    except:
            
        return ('发现异常')
        
if __name__=='__main__':
    url='https://www.amazon.cn/gp/product/B01M8L5Z3Y'
    print(GetHTMLText(url))
    
    
'''
######################################################
"""
#代码的可行性与稳定性,无论什么情况都不会出错.
#图片爬取

import requests
import os 



url='http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg'
root="D://pics//"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('文件已保存')
    else:
        print('文件已存在')
except:
    print('获取失败')
"""
######################################################
'''
#ip位置获取,要知道浏览器后台的api是什么,一般都是提交到链接上

import requests

url='http://m.ip138.com/ip.asp?ip='
r=requests.get(url+'202.204.80.112')


'''

######################################################

'''
#beautifulsoup4的实例解析
import requests 
from bs4 import BeautifulSoup

soup=BeautifulSoup('<p>data</p>','html.parser')     #r.text替代demo
#html.parser属于html解析器,安装bs就可以使用
#lxml解析器,pip install lxml
#xml解析器 pipinstall lxml
#html5lib解析器,pip install html5lib
#4种解析器对应不同格式的文档.
r=requests.get('http://python123.io/ws/demo.html')
demo=r.text
print(soup.prettify())

'''
########################################################
'''

#<p class='title'>...</p>

from bs4 import BeautifulSoup
#标签树->html文档->BeautifulSoup类
#多使用print()函数,环境友好型.
soup=BeautifulSoup(demo,'html.parser')

for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

'''
'''
################################################

#中国大学排名,软科世界大学排名(垃圾)
#定向爬虫,爬取指定url信息,静态网页爬取
#可在主站根目录下查看有无robots.txt文件确认是否可以爬取,无则404nginx
#输出时的中文字符对齐方式,默认是西文字符填充,可更改为中文字符填充chr(12288),空格.
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    
    except:
        return ""
def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])
            
    
def printUnivList(ulist,num):
    tplt="{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名","学校名称","总分",chr(12288)))
    for i in range(num):
        u=ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))
      
        
        
def main():
    uinfo=[]
    url='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20) #20 所大学
#if __name__=="__main__":
main()         #另一种调用方式
'''
###########################################

#爬取额淘宝内容
import requests
import re


def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""
    
    
def parsePage(ilt,html):
    try:
        plt=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt=re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            ilt.append([price,title])
    except:    
        print("") 
    
    
def printGoodsList(ilt):
    tplt="{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))
    
    
def main():
    goods='书包'
    depth=2
    start_url='https://s.taobao.com/search?q='+goods
    infoList=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(44*i)
            html=getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)
    
    
main()
    
