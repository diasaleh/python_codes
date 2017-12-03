# -*- coding: UTF-8 -*-
from __future__ import division
import sys
import xlsxwriter

workbook = xlsxwriter.Workbook('/Users/diasaleh/Desktop/'+str(sys.argv[4])+'avgWordL.xlsx')
worksheet = workbook.add_worksheet()
format = workbook.add_format()
format.set_bold()
format.set_font_color('white')
format.set_bg_color('green')
format.set_font_size(16)
row = 3
row2 = 3
col = 1
size=int(sys.argv[3])+1

def wordAvgLength( str ):
    #
    # sentence=""
    words = sentence.split()
    average = sum(len(word) for word in words) / len(words)
    print average
    return average


sentence=""
avg=0
avgAvg=0
for i in range(1, size):
    f = open(sys.argv[1]+"/"+sys.argv[2]+str(i)+".txt", "r")
    sentence = f.read()
    sentence = unicode(sentence, "utf-8")
    avg=wordAvgLength(sentence)
    worksheet.write(row, col, str(i) , format)
    worksheet.write(row + 1, col, avg, format)
    avgAvg+=avg
    avg=0
    col += 1
    row = 3
print "avg"
row = 5
size=size-1
for k in range(1,101):
    worksheet.write(row, k, avgAvg/size,format)

print avg
workbook.close()