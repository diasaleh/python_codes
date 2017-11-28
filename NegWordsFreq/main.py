# -*- coding: UTF-8 -*-
from __future__ import division
import xlrd
import xlsxwriter
from collections import Counter
from collections import defaultdict

size=1
book = xlrd.open_workbook('/Users/diasaleh/Desktop/GP/neg.xlsx')
sheet = book.sheet_by_name('Sheet1')
workbook = xlsxwriter.Workbook('/Users/diasaleh/Desktop/1000allNegCatNew.xlsx')
worksheet = workbook.add_worksheet()
format = workbook.add_format()
format.set_bold()
format.set_font_color('white')
format.set_bg_color('green')
format.set_font_size(16)
neg = defaultdict(list)
avgNegCount = [0] * sheet.ncols
print sheet.ncols
col=1
roww=1
j=0
for i in range(0,sheet.ncols):
    for row in range(0, sheet.nrows):
        if sheet.cell_value(row, i) != "":
            neg[i].append(sheet.cell_value(row, i))
            j+=1
    j=0
print neg
for i in range(1,size+1):
    f = open("/Users/diasaleh/Desktop/new/100/n (74).txt", "r")
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

    # print words
    # print neg[0][0]
    for j in range(0,sheet.ncols):
        for p in range(0,len(neg[j])):
                # print neg[j][p]
                # print x[k]
                if neg[j][p] in counts:
                     negCount[j]+=counts.get(neg[j][p])
    for j in range(0,sheet.ncols):
        avgNegCount[j]+=(negCount[j])

    for j in range(0,sheet.ncols):
        worksheet.write(roww, col, str(i) +"  " +neg[j][0], format)
        worksheet.write(roww + 1, col, 100*negCount[j]/sum(negCount), format)
        roww +=3

    roww = 1
    col +=1
    print negCount

roww = 3
for j in range(0, sheet.ncols):
    for b in range(1,75):
        worksheet.write(roww, b, 100*avgNegCount[j]/sum(avgNegCount), format)
    roww += 3
workbook.close()
