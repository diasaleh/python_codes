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
ff=open("/Users/diasaleh/Downloads/watan-2004/culture/culture.html/c1.txt","w")
f=codecs.open("/Users/diasaleh/Downloads/watan-2004/culture/culture.html/h1.html", 'r')
text = f.read()
text = text.decode('cp1256')
print text
# text = text.encode('utf-8')
text = regex.sub(ur'[^\p{Arabic}]', u' ', text)
text = re.sub(' +',' ',text)
# text = text.decode("utf-8")
ff.write(text.encode('utf-8'))
ff.close()
f.close()
