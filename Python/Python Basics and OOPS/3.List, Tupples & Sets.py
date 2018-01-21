# List
courses = ['History', 'Science', 'CompSci', 'Physics']

print(courses)

# Length of list
print(len(courses))

# Fetch list using index, it starts with 0
print(courses[2])


# Print Last Item
print(courses[len(courses) - 1])
# Another way
print(courses[-1])

print(courses[-2])  # Print last second item

# List of indexes to display
print(courses[0:2])  # from index 0 to 1 it will display
print(courses[:3])   # will display till index 2
print(courses[2:])   # will display from 2 till end

# Append data in list
courses.append('Art')   # it will insert last in list
print(courses)

courses.insert(0, 'English')   # it will insert data at mentioned position
print(courses)


# List can have list in it as shown below
courses1 = ['History', 'Science', 'CompSci', 'Physics']
courses2 = ['Art', 'Education']

courses1.insert(0, courses2)
print(courses1)

# To insert list of courses2 into courses1 we can use extend command
list1 = ['History', 'Science', 'CompSci', 'Physics']
list2 = ['Art', 'Education']
list1.extend(list2)
print(list1)


# Remove an item from list
courses.remove('Science')
print(courses)

# Another method to remove item from list using POP command, it will remove the element from last as shown below
courses = ['History', 'Science', 'CompSci', 'Physics']
courses.pop()
print(courses)  # As we can see Physics is removed from the last.

# POP command also returns the value which was popped, we can see below
courses = ['History', 'Science', 'CompSci', 'Physics']
popped = courses.pop()
print(popped)   # This returned the popped value
print(courses)

# Want to reverse the list we can use reverse command as shown below
courses = ['History', 'Science', 'CompSci', 'Physics']
courses.reverse()
print(courses)


# Want to sort in ascending order
courses = ['History', 'Science', 'CompSci', 'Physics']
courses.sort()
print(courses)

# Want to sort in descending order
courses = ['History', 'Science', 'CompSci', 'Physics']
courses.sort(reverse=True)
print(courses)


# Want to sort in ascending order without altering the original list
courses = ['History', 'Science', 'CompSci', 'Physics']
sorted_list = sorted(courses)
print(sorted_list)


# Get minimun from the list
num = [1, 5, 3, 2, 4]
print(min(num))

# Get maximum from the list
num = [1, 5, 3, 2, 4]
print(max(num))

# Get sum of the whole list
num = [1, 5, 3, 2, 4]
print(sum(num))

# Search the index of any known data from list
courses = ['History', 'Science', 'CompSci', 'Physics']
print(courses.index('CompSci'))  # It returned as it starts from 0

# Check if an item is in the list we will use IN function
print('Science' in courses)  # Returns true as it is in the list
print('Art' in courses)     # Returns false as it is not in the list

# To print items in courses
courses = ['History', 'Science', 'CompSci', 'Physics']

for item in courses:
    print(item)

# To print with index
for index, item in enumerate(courses):
    print(index, item)

# To print with index 1
for index, item in enumerate(courses, start=1):
    print(index, item)

# Convert list into string
courses = ['History', 'Science', 'CompSci', 'Physics']
course_str = ' - '.join(courses)
print(course_str)

# Convert string into list
new_list = course_str.split(' - ')
print(new_list)

# Tuple, if we define a tuple we can not change it later on as they are fixed by defination
tuple_1 = ('History', 'Science', 'CompSci', 'Physics')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Art'
# print(tuple_1)  # This will throw error as it is tuple by defination

# Now we will see the sets
cs_courses = {'History', 'Science', 'CompSci', 'Physics', 'Science'}
print(cs_courses)   # every time we run print the data will not show in order, it will be randomized
# Also we can not add duplicate values in sets, as we have added Science 2 times it will display one only.

# Print intersection
cs_courses = {'History', 'Science', 'CompSci', 'Physics'}
art_courses = {'History', 'Science', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))  # It displayed the common value which both the courses contain

# Print difference
print(cs_courses.difference(art_courses))  # It displayed the value which are in cs_courses but not in art_courses

# Print all the courses
print(cs_courses.union(art_courses))  # It displayed all the courses of both the sets
