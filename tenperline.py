"""Read a sequence of integers between 0 and 99 and write 10 integers per line, with columns aligned"""

import sys
import stdarray
import stdio
import random
import math

while not stdio.isEmpty():
    for i in range(10):
        value = stdio.readInt()
        if value >= 0 and value <= 99:
            stdio.writef('%2d ', value)
    stdio.writeln()