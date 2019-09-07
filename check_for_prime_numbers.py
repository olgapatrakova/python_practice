check_prime = [26, 39, 51, 53, 57, 79, 85]

### Check if each number is a prime number and show an appropriate result
for number in range(len(check_prime)):
    if check_prime[number] % 2 == 0:
        print("{} is not a prime number, because 2 is a factor of {}".format(check_prime[number], check_prime[number]))
    elif check_prime[number] % 3 == 0:
        print("{} is not a prime number, because 3 is a factor of {}".format(check_prime[number], check_prime[number]))
    elif check_prime[number] % 5 == 0:
        print("{} is not a prime number, because 5 is a factor of {}".format(check_prime[number], check_prime[number]))
    elif check_prime[number] % 7 == 0:
        print("{} is not a prime number, because 7 is a factor of {}".format(check_prime[number], check_prime[number]))
    else:
        print("{} is a prime number".format(check_prime[number]))