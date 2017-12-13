# -*- coding: utf-8 -*-
import re
import regex
import chardet
import string
import collections

i=1
t=""
for i in range(1,69):
	print i
	f=open("/Users/diasaleh/Desktop/courpos/ForShell/1000/TN"+str(i)+".txt","r")
	text = f.read()
	# text = unicode(text, "utf-8")
	t+=text
	f.close()
words = t.split()
s=1
e=1
text=""
slices = len(words)/500
print len(words)
for i in range(0,slices):
	s=i*500
	e=s+500
	for j in range(s,e):
		text+=words[j]+" "
	out = open("/Users/diasaleh/Desktop/courpos/divided500/1000/TN"+str(i)+".txt","w")
	out.write(text)
	out.close()
	text=""

