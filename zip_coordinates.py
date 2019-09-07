x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
### Specify the label and coordinates of each point in a string

for coordinate in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(coordinate[0], coordinate[1], coordinate[2], coordinate[3]))

print(points)