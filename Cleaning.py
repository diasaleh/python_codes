# -*- coding: utf-8 -*-
import re
import regex
import chardet
import string
import xlsxwriter
import collections

tashkeel_patt = ur"[\u0617-\u061A\u064B-\u0652]+"
workbook = xlsxwriter.Workbook('/Users/diasaleh/Desktop/test.xlsx')
worksheet = workbook.add_worksheet()
format = workbook.add_format()
format.set_bold()
format.set_font_color('white')
format.set_bg_color('green')
format.set_font_size(16)
text = u'aweerwq\u0645\u0631\u062d\u0628\u0627\u043c\u0438\u0440'
print(text)
text = regex.sub(ur'[^\p{Latin}]', u' ', text)
print(text)
wordsCC=0
i=1
row=3
col=2
digit_list = '٠١٢٣٤٥٦٧٨٩'

regexx = ur'[\u0660-\u0669]+'
subst = u" "
t=""
for i in range(1,11873):
	print i
	f=open("/Users/diasaleh/Desktop/blogs/tb ("+str(i)+").txt","r")
	text = f.read()
	text = text.decode('utf-8')
	text = regex.sub(ur'[\p{Latin}]', u' ', text)
	text =re.sub('[A-Za-z0-9]+', ' ', text)
	text = re.sub(r'[?|$|.|!]',r' ',text)
	text = " ".join(re.findall(ur"[\u0617-\u061A\u064B-\u0652\u0600-\u06FF]+",text))
	text = text.replace("،".decode("utf-8"), " ");
	text = text.replace("؟".decode("utf-8"), " ");
	text = text.replace("ـ".decode("utf-8"), " ");
	text = text.replace("؛".decode("utf-8"), " ");
	text = text.replace(" ".decode("utf-8"), " ");
	text = text.replace("٪".decode("utf-8"), " ");
	
	text = re.sub(regexx, subst, text)

	text = re.sub(' +',' ',text)
	t+=text
	text = text.encode('utf-8')
	out = open("/Users/diasaleh/Desktop/courpos/ForShell/blogs/TN"+str(i)+".txt","w")
	out.write(text)
	out.close()
letters = collections.Counter(t)
for r in letters:
        print r, letters[r]        
        #print "%s : %d" % (k,v)
        worksheet.write(row+1, col, r,format)
        worksheet.write(row+1, col+1, letters[r] ,format)
        row+=1	
workbook.close()