print("Now think of a number from 0 to 100, then press Enter")
input()
print("""
All you have to do is answer to guess
'c' if my guess is 'C'orrect
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number
""")
low = 0
high = 100

while True:
    mid = (low + high) //2
    ans = input("Is {0} your number?: ".format(mid)).upper()

    if ans == 'C':
        print('I know it!')
        break
    elif ans == 'S':
        low = mid
    elif ans == 'L':
        high = mid
    else:
        print("Ezzz")