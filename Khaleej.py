#!/usr/bin/python
# -*- coding: cp1256 -*-
import sys
import codecs
import re
import regex
import chardet
text = u'aweerwq\u0645\u0631\u062d\u0628\u0627\u043c\u0438\u0440'
print(text)
text = regex.sub(ur'[^\p{Arabic}]', u' ', text)
print(text)
wordsCC=0
for i in range(1,101):
	wordsCA = 0
	out = 	open("/Users/diasaleh/Desktop/KhaleejM/TN"+str(i)+".txt","a")
	print "========================================"
	print i
	for j in range(1,10):
		f=codecs.open("/Users/diasaleh/Downloads/Khaleej-2004/Economy/e"+str(j+((i-1)*9))+".html", 'r')
		text = f.read()
		print text
		text = text.decode('cp1256')
		text = regex.sub(ur'[^\p{Arabic}]', u' ', text)
                text = re.sub(' +',' ',text)
		text = text.encode('utf-8')
		x = text.split()
		wordsC = sum(len(xi) > 1 for xi in x)
		print wordsC
		wordsCA += wordsC
    	        out.write(text)
		out.write("\n \n")
		print "/Users/diasaleh/Downloads/Khaleej-2004/Economy/e"+str(j+((i-1)*9))+".html"
		f.close()
	for j in range(1,10):
		f=codecs.open("/Users/diasaleh/Downloads/Khaleej-2004/International/i"+str(j+((i-1)*9))+".html", 'r')
		text = f.read()
		text = text.decode('cp1256')
		text = regex.sub(ur'[^\p{Arabic}]', u' ', text)
                text = re.sub(' +',' ',text)
		text = text.encode('utf-8')
		x = text.split()
                wordsC = sum(len(xi) > 1 for xi in x)
		print wordsC
		wordsCA += wordsC    	
		out.write(text)
		out.write("\n \n")
		print "/Users/diasaleh/Downloads/Khaleej-2004/International/i"+str(j+((i-1)*9))+".html"
		f.close()
	for j in range(1,24):
		f=codecs.open("/Users/diasaleh/Downloads/Khaleej-2004/Local/l"+str(j+((i-1)*23))+".html", 'r')
		text = f.read()
		text = text.decode('cp1256')
		text = regex.sub(ur'[^\p{Arabic}]', u' ', text)
                text = re.sub(' +',' ',text)
		text = text.encode('utf-8')
		x = text.split()
                wordsC = sum(len(xi) > 1 for xi in x)
		print wordsC
		wordsCA += wordsC    	
		out.write(text)
		out.write("\n \n")
		print "/Users/diasaleh/Downloads/Khaleej-2004/Local/l"+str(j+((i-1)*23))+".html"
		f.close()
	for j in range(1,15):
		f=codecs.open("/Users/diasaleh/Downloads/Khaleej-2004/Sports/s"+str(j+((i-1)*14))+".html", 'r')
		text = f.read()
		text = text.decode('cp1256')
		text = regex.sub(ur'[^\p{Arabic}]', u' ', text)
                text = re.sub(' +',' ',text)
		text = text.encode('utf-8')
		x = text.split()
                wordsC = sum(len(xi) > 1 for xi in x)
		print wordsC
		wordsCA += wordsC    	
		out.write(text)
		out.write("\n \n")
		print "/Users/diasaleh/Downloads/Khaleej-2004/Sports/s"+str(j+((i-1)*14))+".html"
		f.close()
	wordsCC+=wordsCA
	print wordsCA	
	wordsCA = 0				
	out.close()	
print wordsCC
			