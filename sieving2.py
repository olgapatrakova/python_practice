"""Write the contents of a two-dimentional array of booleans,
using * to represent True and a space to represent False"""

import sys
import stdarray
import stdio
import random
import math

n = 20
a = stdarray.create2D(n+1,n+1,True)
for i in range(2, n+1):
    for j in range(i, n+1):
        if i==j:
            a[i][j]=False
        else:
            for k in range(2, n+1):
                if i % k == 0 and j % k == 0:
                    a[i][j] = False
                    a[j][i] = False

stdio.writeln(a)
for i in range(n):
    for j in range(n):
        if a[i][j] == True:
            stdio.write('*')
        else:
            stdio.write(' ')
    stdio.writeln()