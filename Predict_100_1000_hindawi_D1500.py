# -*- coding: utf-8 -*-
from __future__ import division
import codecs
import xlrd
import xlsxwriter
from collections import Counter
from collections import defaultdict
import sys
import numpy as np
import pickle

# size=int(sys.argv[3])+1
cat1="hindawi"
cat2=1000
cat3=100
fn=7
farasaFeat = [6,18,26,38,42,54]
book1_1 = xlrd.open_workbook('/Users/diasaleh/Desktop/'+(cat1)+'D_shell_output/'+str(cat1)+'DPOS.xlsx')
sheet1_1 = book1_1.sheet_by_name('Sheet1')

book1_2 = xlrd.open_workbook('/Users/diasaleh/Desktop/'+(cat1)+'D_shell_output/'+str(cat1)+'DavgWordL.xlsx')
sheet1_2 = book1_2.sheet_by_name('Sheet1')

book2_1 = xlrd.open_workbook('/Users/diasaleh/Desktop/'+str(cat2)+'D_shell_output/'+str(cat2)+'DPOS.xlsx')
sheet2_1 = book2_1.sheet_by_name('Sheet1')

book2_2 = xlrd.open_workbook('/Users/diasaleh/Desktop/'+str(cat2)+'D_shell_output/'+str(cat2)+'DavgWordL.xlsx')
sheet2_2 = book2_2.sheet_by_name('Sheet1')

book3_2 = xlrd.open_workbook('/Users/diasaleh/Desktop/'+str(cat3)+'D_shell_output/'+str(cat3)+'DavgWordL.xlsx')
sheet3_2 = book3_2.sheet_by_name('Sheet1')

book3_1 = xlrd.open_workbook('/Users/diasaleh/Desktop/'+str(cat3)+'D_shell_output/'+str(cat3)+'DPOS.xlsx')
sheet3_1 = book3_1.sheet_by_name('Sheet1')

size1 = 3
size2 = 3
size3 = 3
print size1
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
xCat1test=np.dstack((featuresCat1)).reshape(-1,fn)
xCat2test=np.dstack((featuresCat2)).reshape(-1,fn)
xCat3test=np.dstack((featuresCat3)).reshape(-1,fn)

print len(xCat1test)

print len(xCat2test)

print len(xCat3test)

from sklearn.naive_bayes import GaussianNB
f = open('NB_100_1000_hindawi_D1500.pickle', 'rb')
clf = pickle.load(f)
f.close()
print(clf.score(xCat1test,np.repeat("hindawi",len(xCat1test))))

print(clf.predict(xCat1test))
# print(clf.predict_proba(xCat1test))
print("====================================")

print(clf.predict(xCat2test))
# print(clf.predict_proba(xCat2test))
print(clf.score(xCat2test,np.repeat("1000",len(xCat2test))))

print("====================================")
# print "1000"


print(clf.predict(xCat3test))
# print(clf.predict_proba(xCat3test))
print(clf.score(xCat3test,np.repeat("100",len(xCat3test))))


