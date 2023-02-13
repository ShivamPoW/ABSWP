import shelve      # Stores python in Binary

# Open shell files
shFile = shelve.open('./8_Files/dat')
shFile['sqroots'] = [1.414, 1.732, 2, 2.236]
shFile.close()

# print 
shFile = shelve.open('./8_Files/dat')
print(shFile['sqroots'])

# keys
print(list(shFile.keys()))

# values
print(list(shFile.values()))

shFile.close()