"""Read n floats and write their mean (average value) and standard deviation."""

import sys
import stdarray
import stdio
import random
import math

n = int(sys.argv[1])
total = 0
difference = 0
for i in range(n):
    value = stdio.readFloat()
    total += value
    average = total / (i+1)
    difference += (value - average) ** 2
deviation = math.sqrt(difference) / n
stdio.writeln(average)
stdio.writeln(deviation)
