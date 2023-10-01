#!/usr/bin/env python
import os
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
                mdates.append((int(r[5]),int(r[4])))
    print('The End of file',file)
mdates=set(mdates) # to make unique
mdates=list(mdates)   
mdates.sort()
print(mdates)
