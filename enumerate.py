cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

### Modify the cast so that each element contains the name followed by the character's corresponding height
for person in enumerate(cast):
    cast[person[0]] = "{} {}".format(person[1], heights[person[0]])

print(cast)