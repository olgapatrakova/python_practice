points = 55

### Establish the default prize value to None
prize = None

### Use the points value to assign prizes to the correct prize names
if points <= 50:
    prize = "wooden rabit"
elif points <= 150:
    prize = None
elif points <= 180:
    prize = "wafer-thin mint"
else:
    prize = "penguin"

### Use the truth value of prize to assign result to the correct prize
if prize:
    result = "Congratulations! You won a {}!".format(prize)
else:
    result = "Oh dear, no prize this time."

print(result)