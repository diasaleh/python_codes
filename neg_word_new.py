# -*- coding: UTF-8 -*-
from __future__ import division
import xlrd
import xlsxwriter
from collections import Counter
from collections import defaultdict
import sys
def createList():
    nsufff={}
    for i in range(1,size):
        with open('/Users/diasaleh/Desktop/'+(sys.argv[4])+'_shell_output/Farasa_details/Farasa_POS_Type_2_'+str(i)+'.txt', "r") as f:
            for line in f:
                x = line.split("&")
                nsufff[x[0]]=0
    return nsufff
size=int(sys.argv[3])+1
book = xlrd.open_workbook('/Users/diasaleh/Desktop/GP/neg.xlsx')
sheet = book.sheet_by_name('Sheet1')
workbook = xlsxwriter.Workbook('/Users/diasaleh/Desktop/'+(sys.argv[4])+'_shell_output/'+(sys.argv[4])+'NegCat_New.xlsx')
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
negCount=[0]*sheet.ncols
for i in range(0,sheet.ncols):
    for row in range(0, sheet.nrows):
        if sheet.cell_value(row, i) != "":
            neg[i].append(sheet.cell_value(row, i))
            j+=1
    j=0
print neg
NSUFFall=createList()
for i in range(1,size):
    nsuff = createList()
    with open('/Users/diasaleh/Desktop/'+(sys.argv[4])+'_shell_output/Farasa_details/Farasa_POS_Type_2_'+str(i)+'.txt', "r") as f:
        for line in f:
            x = line.split("&")
            nsuff[x[0]]+=1
    allPron = sum(nsuff.values())

    # print words
    print neg[0][0]
    for j in range(0,sheet.ncols):
        for p in range(0,len(neg[j])):
                # print neg[j][p]
                # print x[k]
                if neg[j][p] in nsuff:
                     negCount[j]+=nsuff.get(neg[j][p])
    for j in range(0,sheet.ncols):
        avgNegCount[j]+=(negCount[j])

    for j in range(0,sheet.ncols):
        worksheet.write(roww, col, str(i) +"  " +neg[j][0], format)
        worksheet.write(roww+1, col, negCount[j], format)
        if sum(negCount) !=0:
            worksheet.write(roww + 2, col, 100*negCount[j]/sum(negCount), format)
        roww +=4
    print negCount

    negCount = [0] * sheet.ncols

    roww = 1
    col +=1

roww = 4
for j in range(0, sheet.ncols):
    for b in range(1,75):
        worksheet.write(roww, b, 100*avgNegCount[j]/sum(avgNegCount), format)
    roww += 4
workbook.close()
