"""Write the transposition of a two-dimentional array"""

import sys
import stdarray
import stdio
import random
import math

a = [[99, 98, 92, 94, 99, 90, 76, 92, 97, 89],
     [85, 57, 77, 32, 34, 46, 59, 66, 71, 29],
     [98, 78, 76, 11, 22, 54, 88, 89, 24, 38]]

b = stdarray.create2D(10, 3, 0)

for i in range(10):
    for j in range(3):
        b[i][j] = a[j][i]
stdio.write(b)
