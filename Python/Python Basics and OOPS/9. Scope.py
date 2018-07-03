'''
LEGB
Local, Enclosing, Global, Built-in
Local can be inside a function or class method, for example.
Enclosed can be its enclosing function, e.g., if a function is wrapped inside another function.
Global refers to the uppermost level of the executing script itself, and
Built-in are special names that Python reserves for itself.
'''


# x='global x'

def test():
    global x  # we are explicitly setting x as global from here
    y = 'local y'
    x = 'local x'
    # print(y)
    print(x)


test()
# print(y)  # This will through name error as y is defined in test function only
print(x)

import builtins

print(dir(builtins))  # for getting built-in modules


# Explaning enclosing now
def outer():
    x = 'outer x'

    def inner():
        # nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()
