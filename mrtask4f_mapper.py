
#Q6 Calculate the average trip revenue per month?


import sys
import errno

try:
    for line in sys.stdin:
        line = line.strip()
        line = line.split(",")

        if line[0] != "tpep_pickup_datetime" and line[0] != "":
            Month=str(line[9])
            print ('%s' % (Month))

except IOError as e:
    if e.errno == errno.EPIPE:
        pass