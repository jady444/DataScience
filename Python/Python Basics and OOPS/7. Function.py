def hello_func():  # creating normal function
    print('Hello Function!')


hello_func()


def hello():  # creating return value function
    return 'Hello Function! Return value'


print(hello())


def hello(greeting):  # creating return value function with argument
    return '{} World'.format(greeting)


print(hello('Hello'))


def hello_func(greeting, name='You'):  # function with default value
    return '{}, {}'.format(greeting, name)


print(hello_func('Hello', 'Jay'))  # passed both argument
print(hello_func('Hello'))  # passed only one argument and let other to choose default


def student_info(*args, **kwargs):
    print(args)  # args will store the tuple data
    print(kwargs)  # kwargs will store the dictionary data which we will pass in arguments of function


print(student_info('Math', 'Art', name='John', age=25))

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 25}

student_info(courses, info)  # now the data shown here will be in list and dictionary
student_info(*courses, **info)  # it has now unpack all the args and kwargs

# Sample example of function

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]


print(is_leap(2020))
print(days_in_month(2017, 2))
print(days_in_month(2020, 2))
print(days_in_month(2020, 10))
print(days_in_month(2020, 23))
