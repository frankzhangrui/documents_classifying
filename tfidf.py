import re
import numpy as np
import math
from string import punctuation
import csv
import sys
dol=len(sys.argv)-1
def word2num(word):
    number=0;
    length=len(word)
    for i in range(len(word)):
        if i<length-1:
            dig=word[-1];
            number=number+(ord(dig)-ord('a')+1)*(26**(i));
            word=word[:length-i-1];
        else:
            dig=word[0];
            number=number+(ord(dig)-ord('a')+1)*(26**(length-1));
    return number

def num2word(snum):
    inc=snum
    word=''
    for i in range(len(str(snum))):
        if i==0:
            s,y=divmod(inc,26)
            char=chr(y+ord('a')-1)
            inc=inc-y*(26**(i))
            word=word+char
        else:
            s,y=divmod(s,26)
            char=chr(y+ord('a')-1)
            inc=inc-y*(26**(i))
            word=word+char
    if len(word)==1:
        word=word
    else:
        word=word[::-1]
    word ="".join(c for c in word if c not in punctuation)
    return word
pattern = '[a-zA-Z ]'
L=[None]*dol # 7 is the number of document
for j in range(dol):
    tem=sys.argv[j+1];
    f = open(tem,'r');
    listoffile=f.readlines()
    length=len(listoffile)
#output = ''.join(re.findall(pattern, input))
    input='';
    for i in range(length):
        input+=listoffile[i]
#print(input)
    output = ''.join(re.findall(pattern, input))
    output=output.lower()
#print(output)
    output1=output.split()
#print(output1)
    output2=[None]*len(output1)
    for i in range(len(output1)):
        output2[i]=word2num(output1[i])
    #print(output2)
    L[j]=output2;
#print(L)
fl=[];
for i in range(dol):
    fl.extend(L[i]) # L[i] is the number of each document
#print(fl)
fa=np.array(fl)
fb=np.unique(fa)
#print(fb)
numcols=len(fb)# fb is the unique number array
#fb=fb.reshape((1,numcols))
wordcount=np.ones((numcols,dol))
for i in range(numcols):
    for j in range(dol):
        temnum=fb[i]
        wordcount[i][j]=L[j].count(temnum)
#print(wordcount)
wordcount1=np.zeros((numcols,dol))
for i in range(numcols):
    for j in range(dol):
        if wordcount[i][j]>=1:
            wordcount1[i][j]=1;
        else:
            wordcount1[i][j]=0;
idf=np.zeros((numcols,1))
for i in range(numcols):
    idf[i]=math.log(dol/float(sum(wordcount1[i])))
#print(idf)
df=np.zeros((numcols,dol))
for i in range(numcols):
    for j in range(dol):
        mw=wordcount.max(axis=0);
        df[i][j]=wordcount[i][j]/mw[j]
#print(mw)
#print(df) #tf
tfidf=np.zeros((numcols,dol))
for i in range(numcols):
    for j in range(dol):
        tfidf[i][j]=df[i][j]*idf[i]
#print(tfidf)
L=[ [None]*(dol+1) for i in range(numcols+1) ]
l1=['term']
for i in range(dol):
    l1.append(sys.argv[i+1][0:9])
L[0]=l1
for i in range(numcols):
    L[i+1][0]=num2word(fb[i])
    L[i+1][1:dol+1]=tfidf[i][:]

w=csv.writer(sys.stdout,dialect='excel')

#w=csv.writer(file('finaloutput.csv','wb'),dialect='excel')
w.writerows(L)



