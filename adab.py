#!/usr/bin/python
# -*- coding: cp1256 -*-
import sys
import codecs
import re
import regex
import chardet
# text = u'aweerwq\u0645\u0631\u062d\u0628\u0627\u043c\u0438\u0440'
# print(text)
# text = regex.sub(ur'[^\p{Arabic}]', u' ', text)
# print(text)
wordsCC=0
for i in range(1,101):
	wordsCA = 0
	out = 	open("/Users/diasaleh/Desktop/adabM/adabOld/TN"+str(i)+".txt","a")
	print "========================================"
	print i
	for j in range(1,38):
		f=open("/Users/diasaleh/Downloads/adab/H2/h"+str(j+((i-1)*37))+".txt", 'r')
		text = f.read()
		text = text.decode('cp1256')
		text =re.sub('[A-Za-z0-9]+', ' ', text)
		text = regex.sub(ur'[\p{Latin}]', u' ', text)
		text = re.sub(r'[?|$|.|!]',r' ',text)
		text = " ".join(re.findall(ur"[\u0617-\u061A\u064B-\u0652\u0600-\u06FF]+",text))
		text = text.replace("،".decode("utf-8"), " ");
		text = text.replace("؟".decode("utf-8"), " ");
		text = text.replace("ـ".decode("utf-8"), " ");
		text = text.replace("؛".decode("utf-8"), " ");

		text = re.sub(' +',' ',text)
		text = text.encode('utf-8')
		x = text.split()
		wordsC = sum(len(xi) > 1 for xi in x)
		print wordsC
		wordsCA += wordsC
    		out.write(text)
		out.write("\n \n")
		print "/Users/diasaleh/Downloads/adab/HModern/H ("+str(j+((i-1)*37))+").txt"
		f.close()
	
	wordsCC+=wordsCA
	print wordsCA	
	wordsCA = 0				
	out.close()	
print wordsCC
			