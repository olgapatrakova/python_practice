scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

### Create a list of names that only include those that scored at least 65.
passed = [key for key in scores if scores.get(key) >= 65]
print(passed)