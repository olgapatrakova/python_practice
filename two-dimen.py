"""Print randomly generated boolean matrix"""
import random

import stdarray
import stdio

m = 20
n = 40
a = stdarray.create2D(m, n, 0)
for i in range(m):
    for j in range(n):
        a[i][j] = random.randrange(10)
for i in range(m):
    for j in range(n):
        if a[i][j] > 5:
            a[i][j] = True
        else:
            a[i][j] = False
stdio.writeln(a)
for i in range(m):
    for j in range(n):
        if a[i][j] == True:
            stdio.write('*')
        else:
            stdio.write(' ')
    stdio.writeln()
