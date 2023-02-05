# list is mutable, string is not

str = 'adfdsfsdfdsfds'
print(str[2:5])

# slice, in , not, index works same
# slice to change

str = str[2:3]
print(str+ '\n')

# --------------------------------------
# Refence lists (or mutable value)

spam = [1, 2, 3, 4, 5, 6]
eggs = spam

eggs[1] = 5
print(spam)

#--------------------------------------
# True copy
import copy

cheese = copy.deepcopy(spam) 
cheese[1] = 10
print(spam)


