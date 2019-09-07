### Number to find the factorial of
number = 6   

### Start with the product equal to one
product = 1

list_of_numbers = [1,2,3,4,5,6]
### Find the factorial
for i in range(len(list_of_numbers)):
    product *= list_of_numbers[i]

### Print the factorial of number
print(product)