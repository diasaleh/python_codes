# -*- coding: UTF-8 -*-
sentence=""
for i in range(1,32):
    f = open("/Users/diasaleh/Desktop/GP/1000/TN"+str(i)+".txt", "r")
    print "/Users/diasaleh/Desktop/GP/1000/TN"+str(i)+".txt"
    sentence += f.read()
ff =open("/Users/diasaleh/Desktop/GP/1000/TN_1000_ALL.txt","w")
ff.write(sentence)
ff.close()