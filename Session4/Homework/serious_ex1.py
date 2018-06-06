name = input('Your full name: ')
name = name.lower()
name = name.title()
name = name.strip()
for i in range(len(name)):
    name = name.replace('  ', ' ')
print('Updated:', name)