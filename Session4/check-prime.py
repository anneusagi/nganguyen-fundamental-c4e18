n = int(input("Enter a number:"))

is_prime = True
for i in range(2, n):
    if (n%i == 0):
        is_prime = False
        break


if is_prime == True:
    print("{0} is a prime number".format(n))
else:
    print("{0} is not a a prime number".format(n))