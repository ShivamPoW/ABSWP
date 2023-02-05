supplies = ["pens", "pens", "staplers", "pencil"] # notice " == '

# index
print(supplies.index('pens'))

# append
supplies.append('book')
print(supplies)

# insert
supplies.insert(1, 'chair')
print(supplies)

# remove
supplies.remove('pens')

#--------------------------------------------------------------

# Numeric Sort
num = [1, 4, 5 ,1 , 3, 2]
num.sort()
print(num)

# reverse 
num.sort(reverse=True)
print(num)

# Alphabetic Sort (ASCII betical => Upper > lower)
alpha = ['s', 'r', 'w', 'a']
alpha.sort()
print(alpha)

# Ture Alphabetical Sort
alpha = ['s', 'S', 'r', 'w','A', 'a']
alpha.sort(key=str.lower)              # a == A, s == S
print(alpha)

