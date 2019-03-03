"""Create a two-dimentional array b[][] that is the transpose of an existing m-by-n array a[][]"""

import sys
import stdarray
import stdio
import random
import math
m = 5
n = 3

a = stdarray.create2D(m,n,0)
for i in range(m):
    for j in range(n):
        a[i][j] = random.randrange(1,10)
stdio.writeln(a)

b = stdarray.create2D(n,m,0)
for i in range(n):
    for j in range(m):
        b[i][j] = a[j][i]
stdio.writeln(b)