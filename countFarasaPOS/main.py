# -*- coding: UTF-8 -*-
from __future__ import division
import re
import xlsxwriter
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from math import sqrt
from collections import Counter
from collections import defaultdict
size=31
workbook = xlsxwriter.Workbook('/Users/diasaleh/Desktop/1000NSUFF.xlsx')
worksheet = workbook.add_worksheet()
format = workbook.add_format()
format.set_bold()
format.set_font_color('white')
format.set_bg_color('green')
format.set_font_size(16)

NSUFFc=[0]* 1000
NSUFFall=[0]* 1000
sentence=""
nsuff= []
col=1
roww=1
avgNsuff=0
m=0
for i in range(1,size+1):

    with open("/Users/diasaleh/Desktop/GP/pos1000/newPOSresult_1_1000_"+str(i)+".txt", "r") as f:
        for line in f:
            x = line.split("&")
            if len(x) > 2:
                if x[1] == "NSUFF":
                    NSUFFc[i-1] = NSUFFc[i-1] + 1
                    nsuff.append(x[0])
    nsuff.append("+ا")
    nsuff.append("+ان")
    nsuff.append("+ة")
    nsuff.append("+ات")
    nsuff.append("+ون")
    nsuff.append("+ين")
    nsuff.append("+ي")
    nsuff.append("+ان")
    NSUFFc[i-1]+=8
    counts = Counter(nsuff)
    counts = sorted(counts.items())
    print "all"
    print NSUFFc[i-1]
    print "---"
    if len(counts)<8:
        worksheet.write(roww, col, str(i) + "  " + "ا " + str(NSUFFc[i - 1]), format)
        worksheet.write(roww + 1, col, 0, format)
        worksheet.write(roww + 2, col,0, format)
        roww+=4

    for j in range(0,len(counts)):
        print counts[j][1]
        worksheet.write(roww, col, str(i) +"  " +counts[j][0]+" " + str(NSUFFc[i-1]), format)
        worksheet.write(roww + 1, col, 100*counts[j][1]/ NSUFFc[i-1], format)
        worksheet.write(roww + 2, col, counts[j][1], format)
        roww +=4
    roww = 1
    col +=1
    nsuff = []
    counts = Counter(nsuff)

    print "======="
workbook.close()