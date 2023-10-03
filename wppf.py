#!/usr/bin/env python
import os
def  makedic():
    # make dict for each emp and intionalize
    for mdate in mdates:
        empdic[str(mdate[0])+str(mdate[1])]=([0,0])
####################################################

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

mdates=set(mdates) # to make unique
mdates=list(mdates)   
mdates.sort()

mcodes=set(mcodes) # to make unique
mcodes=list(mcodes)   
mcodes.sort()

for code in mcodes:
    tdays=0
    empdic={}
    makedic()
    for mdate in mdates:
        myear  = mdate[0]
        mmonth = mdate[1]
        mfile  = mdate[2]
        with open('data/'+mfile) as txtf:    
            for row in txtf:
                r=row.split('\t')
                if r[0] == code:
                    empdic[str(mdate[0])+str(mdate[1])][0]+=int(r[2])
                    empdic[str(mdate[0])+str(mdate[1])][1]+=int(r[3])
                    tdays +=int(r[2])+int(r[3])
                    break

    print(code,end='\t')
    for row in empdic:
        print(empdic[row][0],empdic[row][1],sep='\t',end='\t')
    print(tdays) ## LF at end of each emp code

print('Total Employees codes',len(mcodes))
