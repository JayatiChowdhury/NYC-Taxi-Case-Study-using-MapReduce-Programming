#Q4: What is the average trip time for different pickup locations?

import sys
import errno

try:
    for line in sys.stdin:
        line = line.strip()
        line = line.split(",")

        if line[13] != "tip_amount" and line[1] != "":
            tip=str(line[13])
            pickup=str(line[7])
            print ('%s\t%s' % (tip,pickup))

except IOError as e:
    if e.errno == errno.EPIPE:
        pass
