"""Create a filter that reads in a sequence of integers and writes the integers,
removing repeated values that appear consecutively"""

import sys
import stdarray
import stdio
import random
import math

a = []
b = []
while not stdio.isEmpty():
    value = stdio.readInt()
    a += [value]
for i in range(len(a)):
    if a[i] != a[i-1]:
        b += [a[i]]
stdio.writeln(b)