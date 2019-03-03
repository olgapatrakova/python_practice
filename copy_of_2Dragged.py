""""Create a two-dimentional array b[][] that is a copy of an existing two-dimentional array a[][]
if a[][] is ragged"""

import stdarray
import stdio
import random

m = 5
a = []
for i in range(m):
    row = stdarray.create1D(random.randrange(2,4), 0)
    for j in range(len(row)):
        row[j] = random.randrange(6)
    a += [row]
stdio.writeln(a)

b = a
stdio.write(b)