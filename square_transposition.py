"""Transpose a square two-dimentional array in place without creating a second array"""

import sys
import stdarray
import stdio
import random
import math
n = 3
a = stdarray.create2D(n,n,0)
for i in range(n):
    for j in range(n):
        a[i][j] = random.randrange(1,10)
stdio.writeln(a)

for i in range(n):
    for j in range(i,n):
        temp = a[i][j]
        a[i][j] = a[j][i]
        a[j][i] = temp
stdio.write(a)