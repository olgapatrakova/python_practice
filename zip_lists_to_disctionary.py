cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

### Create cast with names and heights for each name
cast = {}
for person in zip(cast_names, cast_heights):
    cast[person[0]] = person[1]
print(cast)