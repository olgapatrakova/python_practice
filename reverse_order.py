"""Reverse the order of the elements in a one-dimensional array
without creating another array to hold the result"""
import stdarray
import stdio


a = stdarray.create1D(10, 0)
n = len(a)

for i in range(10):
    a[i] = i*2
stdio.writeln(a)
for i in range(10):
    stdio.write(str(a[n-1-i]) + ' ')