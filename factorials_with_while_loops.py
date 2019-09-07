### Number to find the factorial of
number = 6   

### Start with our product equal to one
product = 1

### Track the current number being multiplied
current = 1

### Take a given number and figure out what its factorial is
while current <= number:
    ### Multiply the product so far by the current number
    product *= current
    ### Increment current with each iteration until it reaches number
    current += 1

### Print the factorial of number
print(product)