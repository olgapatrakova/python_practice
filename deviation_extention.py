""""Write the mean (average value) and standart deviation of n floats from standard input"""

import sys
import stdarray
import stdio
import random
import math

n = int(sys.argv[1])
total = 0
difference = 0
for i in range(n):
    value = stdio.readInt()
    total += value
    average = total / (i+1)
    difference += (value - average) ** 2
    deviation = math.sqrt(difference) / (i+1)
stdio.writeln(deviation)
stdio.writeln()
while deviation > 1.5:
    deviation -= 0.1
    stdio.writeln(deviation)
stdio.writeln()
stdio.writeln(average)


