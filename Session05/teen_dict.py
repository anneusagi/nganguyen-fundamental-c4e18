teencode = {
    "hc": "học",
    "ngta": "người ta",
    "any": "anh người yêu",
    "lm": "làm",
    "ng": "người",
    "stt": "status",
    "eny": "em người yêu",
    "ns": "nói",
    "pt": "phát triển", 
}

while True:
for k in teencode:
    print(k, end="\t")
print()

code = input("Yourcode: ")
if code in teencode:
    print("Translation:", teencode[code])
else:
    print("Not found")
    user_choice = input("Do you want to contribute?").upper()
    if user_choice == "Y":
        translation = input("Your translation:")
        teencode[code] = translation
    else:
        print("Bye")
        break
