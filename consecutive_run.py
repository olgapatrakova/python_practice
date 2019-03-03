"""Find the longest consecutive run of sequence of integers entered by a user"""

import sys
import stdarray
import stdio
import random
import math

a = []
count = 0
maximum = 0
while not stdio.isEmpty():
    value = stdio.readInt()
    a += [value]
for i in range(len(a)):
    if a[i] == a[i-1]:
        count += 1
        if count+1 > maximum:
            maximum = count+1
            repeated = a[i]
    else:
        count = 0
stdio.writeln('Longest run: ' + str(maximum))
stdio.writeln('Consecutive ' + str(repeated) + 's')

