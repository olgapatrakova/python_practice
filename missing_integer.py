"""Read N-1 distinct integers between 1 and n,
and determine the missing integer"""

import sys
import stdio

a = []
n = int(sys.argv[1])
for i in range(n):
    value = stdio.readInt()
    a += [value]
    if a[i] != a[i-1] + 1:
        missing = a[i-1] + 1
stdio.writeln(missing)

