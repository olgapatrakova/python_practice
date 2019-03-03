"""Write the roots of discriminant and give an error if it's negative"""

import math
import sys
import stdio

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

discriminant = b*b - 4*a*c
if a != 0 and discriminant >= 0:
	d = math.sqrt(discriminant)
	stdio.writeln((-b + d) / (2 * a))
	stdio.writeln((-b - d) / (2 * a))
else:
	stdio.writeln('Error')