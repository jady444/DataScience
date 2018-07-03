lang = 'Java'

if lang == 'Python':
    print('Language is Python')
elif lang == 'Java':
    print('Language is Java')
else:
    print('No match')

# Due to above example we have to write many conditional statements we can use boolean expressions in it.

user = 'Admin'
loggen_in = True

if user == 'Admin' and loggen_in:
    print('Admin Page')
else:
    print('Bad creds')

# Is method example
a = [1, 2, 3]
b = [1, 2, 3]
print(a in b)  # it will show false as they are stored in different memory

print(id(a))
print(id(b))
