from random import choice

list_words = ["meticulous", "champion", "hexagon"]
word = choice(list_words)
words = list(word)
new_words = []
for i in range(len(words)):
    x = choice(words)
    new_words.append(x)
    y = words.index(x)
    words.remove(words[y])
print(*new_words)

while True:
    answer = input("Your answer: ")
    if answer != word:
        print("Oop!Try again!")
        break
    else:
        print ("Huraaa!")
        break
