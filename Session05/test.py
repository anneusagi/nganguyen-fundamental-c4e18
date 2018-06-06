# person = ["Quý", 20, 0, "Vĩnh Phúc", 2, ["Manga", "Coding"], 3, 20]

#dictionary
#create
person = {
    "name": "Quý",
    "age": 20,
    "ex": 0,
    "favs": ["Manga", "Coding"],
}

print(person)

# name = person['name']
# print(name)

person['length'] = 20

print(person)

#update
person['length'] = 10

print(person)

#delete

# del person['length']

# key = "age"
# if key in person:
#     print(person[key])
# else:
#     print("not found")

# for k in person:
    # print(k, person[k])

#vòng lặp value vs key
for k, v in person.items():
    print(k,v)

# vòng lặp value
for v in person.value():
    print(v)