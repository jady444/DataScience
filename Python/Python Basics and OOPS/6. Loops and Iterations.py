nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

# Bread condition example in for loops

for num in nums:
    if num == 3:
        print("Found!")
        break
    print(num)  # here it did not went to print statement after break and stoped after break point

# Continue condition example in for loops

for num in nums:
    if num == 3:
        print("Found!")
        continue
    print(num)  # here it found the condition 3 and for it, it displayed "Found" and then continue with the for loop

# Nested loop

nums = [1, 2, 3, 4, 5]
for num in nums:
    for letter in 'abc':
        print(num, letter)

# Built in range function
for i in range(10):  # it will start from 0 and will loop till 9
    print(i)

for i in range(1, 10):  # it will start from 1 and will loop till 9
    print(i)

# While loop example
print("While loop")
x = 0
while x < 10:
    print(x)
    x += 1

# Break in while loop
print("Break in while loop")
x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
