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
	out = 	open("/Users/diasaleh/Desktop/watanM/TN"+str(i)+".txt","a")
	print "========================================"
	print i
	for j in range(1,21):
		f=codecs.open("/Users/diasaleh/Downloads/watan-2004/culture.html/h"+str(j+((i-1)*20))+".html", 'r')
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
		print "/Users/diasaleh/Downloads/watan-2004/culture.html/h"+str(j+((i-1)*20))+".html"
		f.close()
	for j in range(1,34):
		f=codecs.open("/Users/diasaleh/Downloads/watan-2004/economy.html/e"+str(j+((i-1)*33))+".html", 'r')
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
		print "/Users/diasaleh/Downloads/watan-2004/economy.html/e"+str(j+((i-1)*33))+".html"
		f.close()
	for j in range(1,21):
		f=codecs.open("/Users/diasaleh/Downloads/watan-2004/international.html/i"+str(j+((i-1)*20))+".html", 'r')
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
		print "/Users/diasaleh/Downloads/watan-2004/international.html/i"+str(j+((i-1)*20))+".html"
		f.close()
	for j in range(1,36):
		f=codecs.open("/Users/diasaleh/Downloads/watan-2004/local.html/l"+str(j+((i-1)*35))+".html", 'r')
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
		print "/Users/diasaleh/Downloads/watan-2004/local.html/l"+str(j+((i-1)*35))+".html"
		f.close()
	for j in range(1,39):
		f=codecs.open("/Users/diasaleh/Downloads/watan-2004/religion.html/r"+str(j+((i-1)*38))+".html", 'r')
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
		print "/Users/diasaleh/Downloads/watan-2004/religion.html/r"+str(j+((i-1)*38))+".html"
		f.close()	
	for j in range(1,46):
		f=codecs.open("/Users/diasaleh/Downloads/watan-2004/sports.html/s"+str(j+((i-1)*45))+".html", 'r')
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
		print "/Users/diasaleh/Downloads/watan-2004/sports.html/s"+str(j+((i-1)*45))+".html"
		f.close()
	wordsCC+=wordsCA
	print wordsCA	
	wordsCA = 0				
	out.close()	
print wordsCC
			