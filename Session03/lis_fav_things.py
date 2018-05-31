thing1 = "death note"
thing2 = "netflix"
thing3 = "teaching"

listfav = ["death note", "netflix", "teaching" ]

# print("Hi there, here your fav things:", *listfav, sep=',')

# newfav = input("Name one more thing:")

# listfav.append("newfav")
# print(*newfav, sep=",")


# first_item = listfav[0]
# print(first_item)

for index, item in enumerate

position = int(input("Position you want to update?"))

new_position = input("Name your favs you want to replace")

favs[position -1] = new_position

for index, item in enumerate(listfav)
    print ("{0}.{1}".format(index +1, item))