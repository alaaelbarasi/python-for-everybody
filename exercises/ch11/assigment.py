import re
fileName=input('File name:')
try:
    fh=open(fileName)
except:
    print('Try again ):')
    exit()
numlist=list()
for line in fh:
    line=line.rstrip()
    x=re.findall('[0-9]+',line)
    if len(x)>0:
        for num in x:
            num=int(num)
            numlist.append(num)
print(sum(numlist))