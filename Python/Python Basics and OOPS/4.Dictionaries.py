# Example of how dictionay looks

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student)
print(student['name'])  # To display any value

print(student.get('phone'))  # If key is not present in dictionay then it will display none useing get method else it would have thrown error.

print(student.get('phone', 'Not Found'))  # If the key is not found we can set default value for it, as we have set 'Not Found' over here.

# Add a key to the dictionary
student['phone'] = '123456789'
print(student)

# To override over existing dictionary key we can declare the key value after then it will over-ride.
student['name'] = 'James'
print(student)

# Update method for dictionary
student.update({'name': 'James', 'age': 26, 'phone': '9876543210'})
print(student)

#  To delete the key from dictionary
# del student['age']  # To display the result of pop I am commenting it
# print(student)

# We can also use pop method to delete key from dictionary
age = student.pop('age')
print(student)
print(age)

# Print length of the dictionary
print(len(student))  # It shows 3 keys name, courses, phone

# Below will show only keys of dictionary
print(student.keys())

# Below will show keys with data of dictionary
print(student.items())

# It will display all the keys in sequence
for key in student:
    print(key)

# It will display all the keys with data in sequence
for key, value in student.items():
    print(key, ':', value)
