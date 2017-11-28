# -*- coding: UTF-8 -*-
from __future__ import division
import xlrd
import xlsxwriter
from collections import Counter
from collections import defaultdict

size=520
workbook = xlsxwriter.Workbook('/Users/diasaleh/Desktop/1400rich.xlsx')
worksheet = workbook.add_worksheet()
format = workbook.add_format()
format.set_bold()
format.set_font_color('white')
format.set_bg_color('green')
format.set_font_size(16)
col=1
roww=1
avgc=0
for i in range(1,size+1):
    f = open("/Users/diasaleh/Desktop/new/1400/t ("+str(i)+").txt", "r")
    print "/Users/diasaleh/Desktop/GP/100/TN"+str(i)+".txt"
    sentence = f.read()
    x = sentence.split()
    x = map(str.strip, x)
    # print(counts)
    # print len(counts)
    words = len(x)
    print words
    x = [o.decode('utf-8') for o in x]
    counts = Counter(x)
    print len(counts)
    avgc += len(counts)/ words
    worksheet.write(roww , col, i, format)
    worksheet.write(roww +1, col, 100*len(counts)/ words, format)
    roww = 1
    col +=1
    words=0
    sentence=""
    x = sentence.split()
    counts = Counter(x)
roww = 1
col=1
for l in range(1,size+1):
    worksheet.write(roww +2, col+l, 100*avgc/size, format)

workbook.close()
