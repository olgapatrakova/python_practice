"""Dot product of 2 rectangular matrices.
The number of columns in the first matrix must be equal to the number of rows in the second matrix"""

import sys
import stdarray
import stdio
import random
import math
m = 3
n = 4
a = stdarray.create2D(m,n,0)
for i in range(m):
    for t in range(n):
        a[i][t] = random.randrange(1,10)
stdio.writeln(a)

t = 4
p = 3
b = stdarray.create2D(t,p,0)
for r in range (t):
    for j in range(p):
        b[r][j] = random.randrange(1,10)
stdio.writeln(b)


if n == t and m == p:
    q = m
    c = stdarray.create2D(q,q,0)
    for i in range(q):
        for j in range(q):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    stdio.writeln(c)
else:
    stdio.writeln('Error: Dimentions do not satisfy the condition')


