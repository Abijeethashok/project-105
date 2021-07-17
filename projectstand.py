import csv
import math

with open('projectdata.csv',newline = '') as f:
    reader = csv.reader(f)
    datafile = list(reader)

data1 = datafile[0]

def findingmean(meanofdata):
    number = len(meanofdata)

    total = 0 

    for i in meanofdata:
        total = total + int(i)

    findingmean = total/number
    return findingmean

meanlist = []

for x in data1:
    subtractvalue = int(x) - findingmean(data1)
    subtractvalue = subtractvalue * subtractvalue
    meanlist.append(subtractvalue)

addall = 0

for z in meanlist:
    addall = addall + z

n = len(data1)
n = n -1 
 
laststep = addall/n

squareroot = math.sqrt(laststep)

print(squareroot)