# -*- coding: UTF-8 -*-
from __future__ import division
import xlsxwriter
import sys



row = 3
row2 = 3
col = 1
col2 = 3
j=0
size=int(sys.argv[3])+1
import collections
avgcat1=0
avgcat2=0
workbook = xlsxwriter.Workbook('/Users/diasaleh/Desktop/100all_Mjhor_Mhmos_details.xlsx')
worksheet = workbook.add_worksheet()
format = workbook.add_format()
format.set_bold()
format.set_font_color('white')
format.set_bg_color('green')
format.set_font_size(16)

def char_frequency(str1):
    dict = {}
    lett = 0
    for n in str1:
        keys = dict.keys()
        n = n.encode("utf-8")
        if not "?@-:*&^%$#@!;\"()‍ ×  ,ـ.-؛_«»[]}{= \\/~`–،؟".__contains__(n) and not n.isalpha() and not n.isdigit() and not n.isalnum():
            lett = lett+1
            if n in keys:
                dict[n] += 1
            else:
                dict[n] = 1
    return dict,lett
for i in range(1,size):
    f = open(sys.argv[1]+"/"+sys.argv[2]+".txt", "r")
    sentence = f.read()
    sentence = unicode(sentence, "utf-8")
    d,n=char_frequency(sentence)
    # d_view = [ (v,k) for k,v in d.iteritems() ]
    # d_view.sort(reverse=True)

    # print d
    # print n
    od = collections.OrderedDict(sorted(d.items()))
    u=0
    cat1=0
    cat2=0
    cat3=0
    for k, v in od.items():
        #print "%s : %d" % (k,v)
        sentence = unicode(k, "utf-8")
        # مجهورة ( Voiced )(ب، ج، د، ر، ز، ط، ع، غ، ص، ل، م، ن، و، ي)
        if(k =="ع"or k=="غ" or k=="ج"  or k=="ب"  or k=="ض"  or k=="ل"  or k=="ن"  or k=="ر"   or k=="د"  or k=="ز"  or k=="ذ"  or k=="ظ"  or k=="و"  or k=="م"  or k=="ي" ):
            cat1+= float((v*100)/(n* 1.0))
            print v, k

        # مهموسة ( Voiceless ) حروفها : (ف، ح، ث، هـ، ش، خ، ص، س، ك، ت، ق، ط، ء) - عند المحدثين
        elif k == "ت" or k == "س" or k == "ش" or k == "ك" or k == "خ" or k == "ه" or k == "ح" or k == "ص" or k == "ث" or k == "ق" or k == "ف"or k=="ط" :
            cat2 += float((v * 100) / (n * 1.0))
        else:
            cat3 += float((v * 100) / (n * 1.0))
    avgcat1 += cat1
    avgcat2+=cat2
    print i
    print "Mjhor" + str(cat1)
    print "Mhmos" + str(cat2)
    print "============="
    worksheet.write(row, col, str(i) + " Mjhor",format)
    worksheet.write(row+1, col, cat1,format)

    print cat3

    worksheet.write(row+3, col, str(i) +" Mhmos",format)
    worksheet.write(row + 4, col , cat2,format)
    worksheet.write(row+6, col, cat3,format)
    col += 1
    row=3
    # for k, v in od2.items():
    #
    #     #print "%s : %d" % (k,v)
    #     sentence = unicode(k, "utf-8")
    #
    #     worksheet.write(row, col, sentence)
    #     worksheet.write(row, col + 1, float((v*100)/(n* 1.0)), format)
    #     row+=1
worksheet.write(5, 1, avgcat1/size,format)
worksheet.write(8, 1, avgcat2/size,format)

workbook.close()