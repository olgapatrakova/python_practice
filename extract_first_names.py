names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

# Create first_names containing just the first names in lowercase.
first_names = [full_name.lower().split(" ")[0] for full_name in names]
print(first_names)