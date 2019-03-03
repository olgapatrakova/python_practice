"""Create a three-dimentional n-by-n-by-n array of booleans,
with each element initialized to False"""

import sys
import stdarray
import stdio
import random
import math
n = 2
a = [[[False]*n]*n]*n
stdio.writeln(a)

b = []
for i in range(n):
    c = stdarray.create2D(n,n,False)
    b += [c]
stdio.writeln(b)