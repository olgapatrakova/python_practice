"""Write n uniform random numbers between 0 and 1,
and writes their average value, their minimum value, and their maximum value."""

import sys
import stdio
import random

n = int(sys.argv[1])
sum = 0
maximum = 0
minimum = 1
for i in range (n):
	r = random.random()
	stdio.writeln(r)
	sum += r
	if maximum > r:
		maximum = maximum
	else:
		maximum = r
	if minimum < r:
		minimum = minimum
	else:
		minimum = r
ave = sum / n
stdio.writeln(ave)
stdio.writeln(minimum)
stdio.writeln(maximum)