#Q2: Which pickup location generates the most revenu
import sys
vender_1=0
vender_2=0
pu=[]
tot={}
for line in sys.stdin:
    i=0
    line = line.strip()
    pickup, charge = line.split("\t")

    if pickup!= "PULocationID":
        if pickup not in pu:
            pu.append(pickup)
            tot[pickup] = float(charge)

        else:
            i=float(tot[pickup])
            i=i+float(charge)
            tot.update({pickup: i})

keymax=str(max(zip(tot.values(), tot.keys()))[1])
valmax=str(max(zip(tot.values(), tot.keys()))[0])
#print(tot)
print(keymax+" : "+valmax)
