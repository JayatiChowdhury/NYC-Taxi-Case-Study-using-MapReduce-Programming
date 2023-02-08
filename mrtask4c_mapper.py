
#Q:3  What are the different payment types used by customers and their count?


import sys
import errno

try:
    for line in sys.stdin:
        line = line.strip()
        line = line.split(",")

        if line[0] != "payment_type" and line[0] != "":
            Payment=str(line[9])
            print ('%s' % (Payment))

except IOError as e:
    if e.errno == errno.EPIPE:
        pass
