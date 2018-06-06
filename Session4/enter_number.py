s = input("Enter your sequence of numbers, separated by space:")

words = s.strip().split(" ")

numbers = []

for item in words:
    numbers.append(int(item))

print(numbers)

