print("Hi there, this is a superuser gateway")

count = 0

while True:
    username = input("username:")
    if username == "c4e":
        password = input("password:")
        if password == "codethechange":
            print("Welcome!")
            break
        else:
            print("password incorrect")
    else:
        print("you are not a superuser")

    count += 1
    if count == 3:
        print("you failed to login 3 times, go away!")
        break