import my_module as mm  # imported python file as module with sub-name
import sys  # imported sys module for path
import random  # generating random data

courses = ['History', 'Math', 'Physics', 'CompSci']
index = mm.find_index(courses, 'Math')
print(index)
print(sys.path)
random_course = random.choice(courses)
print(random_course)
