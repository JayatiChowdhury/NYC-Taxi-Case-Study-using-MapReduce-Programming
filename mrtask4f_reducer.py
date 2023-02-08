


#Q6 Calculate the average trip revenue per month?

import sys
import operator as op
pu=[]
pay=[]
tot={}
for line in sys.stdin:

    line = line.strip()
    pay.append(line)
    if line!= "tpep_pickup_datetime":
        if line not in pu:
            pu.append(line)
pu.sort()
for i in range(len(pu)):
    y=pu[i]
    tot[y]= int(op.countOf(pay,y))
#print(pay)
print(tot)
