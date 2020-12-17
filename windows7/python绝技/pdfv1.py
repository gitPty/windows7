# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 08:37:47 2019

@author: Administrator
"""

#用法:%run pdfv1.py -F Python灰帽子.pdf
#此脚本用于对pdf文件的操作,获取欧迪芬文件元数据,包括作者姓名,建制时间,对多个文件检索出特定作者的操作.
import optparse
import PyPDF2
from PyPDF2 import PdfFileReader


def printMeta(fileName):
    pdfFile=PdfFileReader(open(fileName,'rb'))
    docInfo=pdfFile.getDocumentInfo()
    print('[*] PDF MetaData For : '+str(fileName))
    for metaItem in docInfo:
        print('[+] ' +metaItem +':'+docInfo[metaItem])
        
def main():
    parser=optparse.OptionParser('usage %prog '+'-F <PDF file name>')
    parser.add_option('-F',dest='fileName',type='string',help='specify PDF file name')
    (options,args)=parser.parse_args()
    fileName=options.fileName
    if fileName == None:
        print(parser.usage)
        exit(0)
    else:
        printMeta(fileName)
if __name__=='__main__':
    main()