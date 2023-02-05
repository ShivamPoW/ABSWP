spam = 20 # global

def eggs():
    spam = 42 # local

print(spam)
eggs()
print(spam)

# --------------------------------------
print()


def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

# --------------------------------------
print()


def spam():
    print(eggs)

eggs = 42 
spam()

# --------------------------------------
print()


def spam():
    global eggs  # comment this
    eggs = 20
    print(eggs)

eggs = 42 
spam()
print(eggs)
