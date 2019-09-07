names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

### Create a usernames list
for name in names:
    usernames.append(name.lower().replace(" ", "_"))

print(usernames)