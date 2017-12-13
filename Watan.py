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
i=1
wordsCA=0

for j in range(1,910):
	out = open("/Users/diasaleh/Desktop/courpos/ForShell/Khaleej/TN"+str(i)+".txt","w")
	f=codecs.open("/Users/diasaleh/Downloads/Khaleej-2004/Economy/e"+str(j)+".html", 'r')
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
	print "/Users/diasaleh/Downloads/watan-2004/economy.html/e"+str(j)+".html"
	f.close()
	i+=1
	print i
for j in range(1,954):
	out = open("/Users/diasaleh/Desktop/courpos/ForShell/Khaleej/TN"+str(i)+".txt","w")
	f=codecs.open("/Users/diasaleh/Downloads/Khaleej-2004/International/i"+str(j)+".html", 'r')
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
	i+=1
	print i
	print "/Users/diasaleh/Downloads/Khaleej-2004/international/i"+str(j)+".html"
	f.close()
for j in range(1,2399):
	out = open("/Users/diasaleh/Desktop/courpos/ForShell/Khaleej/TN"+str(i)+".txt","w")
	f=codecs.open("/Users/diasaleh/Downloads/Khaleej-2004/Local/l"+str(j)+".html", 'r')
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
	i+=1
	print i
	print "/Users/diasaleh/Downloads/Khaleej-2004/local.html/l"+str(j)+".html"
	f.close()

for j in range(1,1431):
	out = open("/Users/diasaleh/Desktop/courpos/ForShell/Khaleej/TN"+str(i)+".txt","w")
	f=codecs.open("/Users/diasaleh/Downloads/Khaleej-2004/Sports/s"+str(j)+".html", 'r')
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
	print "/Users/diasaleh/Downloads/Khaleej-2004/sports.html/s"+str(j)+".html"
	f.close()
	i+=1
	print i
wordsCC+=wordsCA
print wordsCA	
wordsCA = 0				
out.close()	
print wordsCC
			