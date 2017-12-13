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
cat1="hindawi"
cat2=1400
cat3=1000
fn=7
farasaFeat = [6,18,26,38,42,54]
book1_1 = xlrd.open_workbook('/Users/diasaleh/Desktop/'+str(cat1)+'_shell_output/'+(cat1)+'POS.xlsx')
sheet1_1 = book1_1.sheet_by_name('Sheet1')

book1_2 = xlrd.open_workbook('/Users/diasaleh/Desktop/'+str(cat1)+'_shell_output/'+(cat1)+'avgWordL.xlsx')
sheet1_2 = book1_2.sheet_by_name('Sheet1')

book2_1 = xlrd.open_workbook('/Users/diasaleh/Desktop/'+str(cat2)+'_shell_output/'+str(cat2)+'POS.xlsx')
sheet2_1 = book2_1.sheet_by_name('Sheet1')

book2_2 = xlrd.open_workbook('/Users/diasaleh/Desktop/'+str(cat2)+'_shell_output/'+str(cat2)+'avgWordL.xlsx')
sheet2_2 = book2_2.sheet_by_name('Sheet1')

book3_2 = xlrd.open_workbook('/Users/diasaleh/Desktop/'+str(cat2)+'_shell_output/'+str(cat2)+'avgWordL.xlsx')
sheet3_2 = book3_2.sheet_by_name('Sheet1')

book3_1 = xlrd.open_workbook('/Users/diasaleh/Desktop/'+str(cat3)+'_shell_output/'+str(cat3)+'POS.xlsx')
sheet3_1 = book3_1.sheet_by_name('Sheet1')

size1 = sheet1_1.ncols
size2 = sheet2_1.ncols
size3 = sheet3_1.ncols
featuresCat1 = np.zeros(shape=(fn,size1-2))
featuresCat2 = np.zeros(shape=(fn,size2-2))
featuresCat3 = np.zeros(shape=(fn,size3-2))
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

row=0
fo= open("/Users/diasaleh/Downloads/test.txt","w")
for col in range(1, size3-1):
		# print sheet.cell_value(farasaFeat[row], col)
		featuresCat3[row][i] = (float(sheet3_2.cell_value(4, col)))
		i+=1
i=0
row+=1

for row in range(1,len(farasaFeat)+1):
	# print row
	# print farasaFeat[row]
	for col in range(2, size3):
		# print sheet2.cell_value(farasaFeat[row], col)
		featuresCat3[row][i] = (float(sheet3_1.cell_value(farasaFeat[row-1], col)))
		i+=1
	i=0	
i=0	


# # featureNew = feature.reshape(3,5)	
# print featuresCat1
# # print len(featuresCat2[0])
# print (featuresCat2[0])
xCat1=np.dstack((featuresCat1)).reshape(-1,fn)
xCat2=np.dstack((featuresCat2)).reshape(-1,fn)
xCat3=np.dstack((featuresCat3)).reshape(-1,fn)
print len(xCat1)
xCat1test=xCat1[:20]
xCat1=xCat1[20:]
print len(xCat1test)
print len(xCat1)
print len(xCat2)
xCat2test=xCat2[:20]
xCat2=xCat2[20:]
print len(xCat2test)
print len(xCat2)
xCat3test=xCat3[:10]
xCat3=xCat3[10:]
print len(xCat3test)
print len(xCat3)
print len(xCat3)
X=np.concatenate((xCat1,xCat2,xCat3),axis=0)
yCat1 = np.repeat("hindawi",len(xCat1))
yCat2=np.repeat(1400,len(xCat2))
yCat3=np.repeat(1000,len(xCat3))
Y=np.concatenate((yCat1,yCat2,yCat3),axis=0)

from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X, Y)
print(clf.score(xCat1test,np.repeat(100,len(xCat1test))))
# print(xCat1test)
print(clf.predict(xCat1test))
# print(xCat2)
print(clf.predict_proba(xCat1test))
print("====================================")

print(clf.predict(xCat2test))
print(clf.predict_proba(xCat2test))
print("====================================")
print "1000"


print(clf.predict(xCat3test))
print(clf.predict_proba(xCat3test))


