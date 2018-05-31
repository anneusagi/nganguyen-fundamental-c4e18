from random import randint

numb = randint(0, 100)
print(numb)

playing  = True
count = 0
while playing:
    if count >= 7:
        print("you lose")
        playing = False
    else:
        guess = int(input("Guess my number(0-100)?"))

        if guess > numb:
            print("A little too large")
        elif guess < numb:
            print("Too small")
        else:
            print("bingo")
            playing = False
    count += 1