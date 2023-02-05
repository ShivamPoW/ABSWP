spam = ['cat', 'dog', 'homan', 'pleb']

# -----------------
# Acess

print (spam[3]) # 3-N (total items)
print (spam[-1])

print(spam[-4]) # 4-N (     ;;    )
print (spam[0])


# ------------------
# Slice

print(spam[1:3])

# ------------------
# Assignment

spam[1] = 'noob'
print(spam)

spam[1:] = ['noob', 'noob', 'noob']
print(spam)

# ------------------
# delete (UnAssignment)

del spam[1]
print(spam)

# ------------------
# length

print(len(spam))

# ------------------
# string to array

l = list('Hommie') 
print(l)

# ------------------
# existence

print('noob' in spam)  # similarly not in