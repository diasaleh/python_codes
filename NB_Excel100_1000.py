# -*- coding: utf-8 -*-
from __future__ import division
import codecs
import xlrd
import xlsxwriter
from collections import Counter
from collections import defaultdict
import sys
import numpy as np

# size=int(sys.argv[3])+1
cat1=100
cat2=1000
fn=7
farasaFeat = [6,18,26,38,42,54]
book1_1 = xlrd.open_workbook('/Users/diasaleh/Desktop/'+str(cat1)+'D_shell_output/'+str(cat1)+'DPOS.xlsx')
sheet1_1 = book1_1.sheet_by_name('Sheet1')

book1_2 = xlrd.open_workbook('/Users/diasaleh/Desktop/'+str(cat1)+'D_shell_output/'+str(cat1)+'DavgWordL.xlsx')
sheet1_2 = book1_2.sheet_by_name('Sheet1')


book2_1 = xlrd.open_workbook('/Users/diasaleh/Desktop/'+str(cat2)+'D_shell_output/'+str(cat2)+'DPOS.xlsx')
sheet2_1 = book2_1.sheet_by_name('Sheet1')
book2_2 = xlrd.open_workbook('/Users/diasaleh/Desktop/'+str(cat2)+'D_shell_output/'+str(cat2)+'DavgWordL.xlsx')
sheet2_2 = book2_2.sheet_by_name('Sheet1')
size1 = sheet1_1.ncols
size2 = sheet2_1.ncols
featuresCat1 = np.zeros(shape=(fn,size1-2))
featuresCat2 = np.zeros(shape=(fn,size2-2))
# print featuresCat1
col=2
row=0
fo= open("/Users/diasaleh/Downloads/test.txt","w")
i=0
for col in range(1, size1-1):
		# print sheet1_2.cell_value(4, col)
		featuresCat1[row][i] = (float(sheet1_2.cell_value(4, col)))
		i+=1
i=0

for row in range(1,len(farasaFeat)+1):
	print row
	# print farasaFeat[row]
	for col in range(2, size1):
		# print sheet1_1.cell_value(farasaFeat[row], col)
		featuresCat1[row][i] = (float(sheet1_1.cell_value(farasaFeat[row-1], col)))
		i+=1
	i=0
i=0

row=0
fo= open("/Users/diasaleh/Downloads/test.txt","w")
for col in range(1, size2-1):
		# print sheet.cell_value(farasaFeat[row], col)
		featuresCat2[row][i] = (float(sheet2_2.cell_value(4, col)))
		i+=1
i=0
row+=1

for row in range(1,len(farasaFeat)+1):
	# print row
	# print farasaFeat[row]
	for col in range(2, size2):
		# print sheet2.cell_value(farasaFeat[row], col)
		featuresCat2[row][i] = (float(sheet2_1.cell_value(farasaFeat[row-1], col)))
		i+=1
	i=0	
i=0	


# # featureNew = feature.reshape(3,5)	
# print featuresCat1
# # print len(featuresCat2[0])
# print (featuresCat2[0])
xCat1=np.dstack((featuresCat1)).reshape(-1,fn)
xCat2=np.dstack((featuresCat2)).reshape(-1,fn)
print len(xCat1)
xCat1test=xCat1[:200]
xCat1=xCat1[200:]
print len(xCat1test)
print len(xCat1)
print len(xCat2)
xCat2test=xCat2[:200]
xCat2=xCat2[200:]
print len(xCat2test)
print len(xCat2)

X=np.concatenate((xCat1,xCat2),axis=0)
yCat1 = np.repeat(100,len(xCat1))
yCat2=np.repeat(1000,len(xCat2))
Y=np.concatenate((yCat1,yCat2),axis=0)

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
print(clf.score(xCat1test,np.repeat(100,len(xCat1test))))
# print(xCat1test)
print(clf.predict(xCat1test))
# print(xCat2)
# print(clf.predict_proba(xCat1test))
print("====================================")

# print(clf.predict(xCat2test))
# print(clf.predict_proba(xCat2test))

print(clf.score(xCat2test,np.repeat(1000,len(xCat2test))))


