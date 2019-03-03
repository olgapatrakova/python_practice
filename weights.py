""""Compute a weighted average of the rows,
where the weights of each score are in a one-dimensional array weights[]."""

import sys
import stdarray
import stdio
import random
import math

grades = [[99.0, 85.0, 98.0],
          [98.0, 57.0, 79.0],
          [92.0, 77.0, 74.0],
          [94.0, 62.0, 81.0],
          [99.0, 94.0, 92.0],
          [80.0, 76.5, 67.0],
          [76.0, 58.5, 90.5],
          [92.0, 66.0, 91.0],
          [97.0, 70.5, 66.5],
          [89.0, 89.5, 81.0]]
weights = [0.25, 0.25, .50]
for i in range(10):
    weighted_average = 0.0
    for j in range(3):
        weighted_average += grades[i][j] * weights[j]
    stdio.writeln(weighted_average)