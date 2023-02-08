#Q4: What is the average trip time for different pickup locations?
import sys
import operator as op

for line in sys.stdin:
    pu=[]

    pay=[]
    tot={}
    tal={}
    line = line.strip()
    tip, pickup = line.split("\t")

    if pickup not in pay:
        pay.append(pickup)
        tot[pickup]=float(tip)

    else:
        i = float(tot[pickup])
        i = i+float(tip)
        tot.update({pickup: i})

for i in range(len(pay)):
    y=pay[i]
    tal[y]= int(op.countOf(pu,y))
dd={}
ans=tot.keys()
q=tot.values()
a=tal.values()
for pra in range(len(tot.keys())):
    dd[ans[pra]]=q[pra]/a[pra]
print(dd)
