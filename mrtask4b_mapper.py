#Q2: Which pickup location generates the most revenue? 
import sys
import errno

try:
    for line in sys.stdin:
        line = line.strip()
        line = line.split(",")

        if line[0] != "PULocationID" and line[0] != "":
            Pickup=str(line[7])
            charge=str(line[16])
            print ('%s\t%s' % (Pickup, charge))

except IOError as e:
    if e.errno == errno.EPIPE:
        pass

