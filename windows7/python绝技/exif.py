# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:26:46 2019

@author: Administrator
"""

import urllib2
from bs4 import BeautifulSoup
from os.path import basename

def downloadImage(imgTag):
    try:
        print('[+] Downloadingimage...')
        imgSrc=imgTag['src']
        imgContent=urllib2.urlopen(imgSrc).read()
        imgFileName=basename(urlsplit(imgSrc)[2])
        imgFile=open(imgFileName,'wb')
        imgFile.write(imgContent)
        imgFile.close()
        return imgFileName
    except:
        return ''

def findImages(url):
    print('[+] Finding images on '+url)
    urlContent=urllib2.urlopen(url).read()
    soup=BeautifulSoup(urlContent)
    imgTags=soup.findAll('img')
    return imgTags


def testForExif(imgFileName):
    try:
        exifData={}
        imgFile=Image.open(imgFileName)
        info=imgFile._getexif()
        if info:
            for (tag,value) in info.items():
                decoded=TAGS.get(tag,tag)
                exifData[decoded]=value
            exifGPS=exifData['GPSIInfo']
            if exifGPS:
                print('[*] '+imgFileName+' contains GPS MEtaData')
    except:
        pass
    