cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

### Define names and heights
names, heights = zip(*cast)

print(names)
print(heights)