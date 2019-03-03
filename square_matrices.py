"""A program computes the product of 2 square matrices of integers."""

import sys
import stdarray
import stdio
import random

n = 3
a = stdarray.create2D(n,n,0)
b = stdarray.create2D(n,n,0)
for i in range(n):
    for j in range(n):
        a[i][j] = random.randrange(1,6)
stdio.writeln(a)
for i in range(n):
    for j in range(n):
        b[i][j] = random.randrange(1,6)
stdio.writeln(b)

c = stdarray.create2D(n,n,0)
for i in range(n):
    for j in range(n):
        for k in range(n):
            c[i][j] += a[i][k] * b[k][j]
stdio.writeln(c)