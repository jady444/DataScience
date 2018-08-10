for i in range(1, 11):
    sentence = 'The value is {}'.format(i)
    print(sentence)

# Format number to print in 01 02 03 like wise, so we are using ":" and then 02 which says that 0 to be there for 2 digits
for i in range(1, 11):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)

for i in range(1, 11):
    sentence = 'The value is {:03}'.format(i)  # This will print the data in 001 002 003
    print(sentence)

pi = 3.14159265

sentence = 'Pi is equal to {}'.format(pi)
print(sentence)

# Now we want to display only first 2 decimial digits the we will use below command
sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)

# To print large number then we can use below command
sentence = '1MB is equal to {:,.2f} bytes'.format(1024 ** 2)
print(sentence)
