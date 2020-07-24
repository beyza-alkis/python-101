# TUPLE
a = (1, 2)
b = (1, 2, 'python', (1, 2))
print(b[2])

# b[2] = 'test' # type error

# List # list ve array aynı şey
x = [1, 2]
b = [1, 2, 'python', x]
print(b[3])
b[3] = [2, 3]
print(b[3])

# Dict
a = {0: 'one', 1: 'two'} # like list
b = {
    'Kevser': 1996,
    'Beyza': 2000
}
print(b['Beyza'])