"""Show the maximum and minimum integer from those entered by a user"""

import stdarray
import stdio

maximum = float('-inf')
minimum = float('inf')

while not stdio.isEmpty():
    value = stdio.readInt()
    if value > maximum:
        maximum = value
    if value < minimum:
        minimum = value
stdio.writeln(maximum)
stdio.writeln(minimum)




