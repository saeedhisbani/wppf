#!/usr/bin/env python
import os
#import subprocess
#result = subprocess.run(["ls -l"], shell=True, capture_output=True, text=True)
#print(result.stdout)
#input()

def finddays(code,mfile):
    mdays,pdays = 0,0
    with open('data/'+mfile) as txtf:
        for row in txtf:
            r=row.split('\t')
            if code == r[0]:
                print(r[2],r[3])
                return r[2],r[3]
        return 0,0
files=[file for file in os.listdir('data') if '.txt' in file]
mcodes=[]
mdates=[]
for file in files:
    with open('data/'+file) as textfile:
        for row in textfile:
            r=row.split('\t')
            if r[0].isnumeric():
                mcodes.append(r[0])
                #r[5] is month r[6] is year
                mdates.append((int(r[5]),int(r[4]),file))
    print('The End of file',file)

mdates=set(mdates) # to make unique
mdates=list(mdates)   
mdates.sort()
for code in mcodes:
    print(code,sep='\t')
    for mdate in mdates:
        myear  = mdate[0]
        mmonth = mdate[1]
        mfile  = mdate[2]
        mdays,pdays = finddays(code,mfile)
        print(mdate[0],mdate[1],mdate[2],sep='\t')
    print() ## LF at end of each emp code
    input()
print(mdates)
#print('LEN Mdates',len(mdates),'Len of Files',len(files))
mcodes=set(mcodes) # to make unique
mcodes=list(mcodes)   
mcodes.sort()
print('T codes',len(mcodes))
