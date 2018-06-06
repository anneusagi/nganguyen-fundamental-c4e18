numbs = [1, 6, 8, 1, 2, 1, 5, 6]
question = int(input("Enter a number: "))

count = 0
for item in numbs:
    if item == question:
        count += 1
print( question,'appears',count,'times in my list')