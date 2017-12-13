# -*- coding: utf-8 -*-
from __future__ import division
import codecs
import xlrd
import xlsxwriter
from collections import Counter
from collections import defaultdict
import sys
import os

# size=int(sys.argv[3])+1
book = xlrd.open_workbook('/Users/diasaleh/Downloads/FinalSortingHinadwi.xlsx')
sheet = book.sheet_by_name('Sheet1')

neg ={}
avgNegCount = [0] * sheet.ncols
col=1
row=1
fo= open("/Users/diasaleh/Downloads/test.txt","w")
negCount=sheet.nrows
# print negCount
i=0
for row in range(0, sheet.nrows):
    # print sheet.cell_value(row, i+1)
    # print sheet.cell_value(row, i)
    t = sheet.cell_value(row, i+1).encode("utf-8").split()
    neg[str(' '.join(t[0:2]))] = (sheet.cell_value(row, i))
    


# for k, v in neg.items():
#     # print ((k) + ' >>> '+ str(v) + '\n\n')
numberOfBox = 1277

books = ""
for i in range(1,numberOfBox):
    print(i)
    text=""
    file = codecs.open('/Users/diasaleh/Desktop/courpos/ForShell/hindawi/TN'+str(i)+'.txt', "r","utf-8")
    text = file.read()
    # text = text.decode("cp1256")
    words = text.split()
    words = [x.encode('utf-8') for x in words]
    # print words
    # print text
    wordsWriter = str(' '.join(words[0:50])).split("تأليف")
    lenWords = len(wordsWriter)
    if lenWords > 1:
        wordsWriter = str(wordsWriter[1]).split()
        wordsTran = str(' '.join(wordsWriter[1:])).split("ترجمة")
        lenWordsTran = len(wordsTran)
        if lenWordsTran > 1:
            wordsTran = str(wordsTran[1]).split()
    else:
        wordsTran = str(' '.join(words[0:50])).split('ترجمة')
        lenWordsTran = len(wordsTran)
        if lenWordsTran > 1:
            wordsTran = str(wordsTran[1]).split()
    
    
    if lenWordsTran > 1:
        if str(' '.join(wordsTran[0:2])).strip()  in neg:
            fo.write(str(neg[str(' '.join(wordsTran[0:2])).strip()]))
            path = "/Users/diasaleh/Desktop/courpos/test/"+str(neg[str(' '.join(wordsTran[0:2])).strip()])
            if not os.path.exists(path):
                os.makedirs(path)
            path += "/"+str(i)+".txt"
            out = open(path,"w+")
            out.write(text.encode('utf-8'))
            out.close()
            fo.write(str(i)+"\n")
        else: 
            path = "/Users/diasaleh/Desktop/courpos/test/error"
            if not os.path.exists(path):
                os.makedirs(path)
            path += "/"+str(i)+".txt"
            out = open(path,"w+")
            out.write(text.encode('utf-8'))
            out.close()   
            fo.write(str(i)+"\n")
    elif lenWords > 1:
        if str(' '.join(wordsWriter[0:2])).strip()  in neg:
            fo.write(str(neg[str(' '.join(wordsWriter[0:2])).strip() ]))
            path = "/Users/diasaleh/Desktop/courpos/test/"+str(neg[str(' '.join(wordsWriter[0:2])).strip()])
            if not os.path.exists(path):
                os.makedirs(path)
            path += "/"+str(i)+".txt"
            out = open(path,"w+")
            out.write(text.encode('utf-8'))
            out.close()
            fo.write(str(i)+"\n")
        else:
            path = "/Users/diasaleh/Desktop/courpos/test/error"
            if not os.path.exists(path):
                os.makedirs(path)
            path += "/"+str(i)+".txt"
            out = open(path,"w+")
            out.write(text.encode('utf-8'))
            out.close()    
            fo.write(str(i)+"\n")
fo.close()  
           
