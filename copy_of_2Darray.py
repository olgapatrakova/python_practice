""""Create a copy of an existing two-dimensional array a[][] if a[][] is rectangular"""

import stdio
import stdarray
import random

m = 3
n = 4
a = stdarray.create2D(m, n, 0)
b = stdarray.create2D(m, n, 0)
for i in range (m):
    for j in range(n):
        a[i][j] = random.randrange(10)
        b[i][j] = a[i][j]

stdio.writeln(a)
stdio.writeln(b)
