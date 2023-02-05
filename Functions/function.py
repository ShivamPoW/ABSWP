def hello(name):
    print(('Hi ' + name + ' ') *3 )   # Newline + None return 

# Any datatype
def sum(a, b):
    return a + b

#int only
def sumInt(a, b):
    return int(a + b)  # add 0

hello('Alice')
print(sumInt(5, 8))
print(sum('hi, ', 'bye.' ))

# --------------------------------------------------------------

# print functions
print('Hello ', end='')
print('World!')
print('Hello','New','World')
print('Hello','New','World',sep=' HEHE ')