# Print Hello World Message
print('Hello World!!!')

# Hello world message with variable
message = 'Hello Python World!!!'
print(message)

# Multi line example
message = """Hello Jay
this is multi-line example"""
print(message)

# Print Length
message = 'Jay Nagar'
print(len(message))

# Print indexes, like 5th character from string
message = 'James Bond'
print(message[4])

# Print text from string in range like from 2 letter to 6th letter
message = 'Justice League'
print(message[1:5])
print(message[6:])  # this will start from 7th character and will display till end
print(message[:5])  # this will start the string from staring and will display till 6th character
print(message[2:-1])    # this means it will start from 3rd character and display till last second character

# Upper case and lower case
message = 'PyThoN'
print(message.lower())  # lower case all the characters
print(message.upper())  # upper case all the characters

# Find index where the character or word starts from
message = 'Hello World'
print(message.find('lo'))
print(message.find('world'))    # returns -1 as the word/letter does not match

# Replace the string
message = 'Hello World'
print(message.replace('World', 'Universe'))

# or we can use below method for string replace
my_message = message.replace('World', 'Universe')
print(my_message)

# concanate string
greeting = 'Hello'
name = 'Jay'

message = '{}, {}. Welcome!!'.format(greeting, name)
print(message)

message = f'{greeting}, {name}. Welcome!!'  # direct passing variable
print(message)
