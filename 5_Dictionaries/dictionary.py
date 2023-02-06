# key Value, unordered (Mutable just like lists)

myCat  = {'size': 'fat',
          'color': 'black',
          'sound': 'Meow'
         }

line = 'My cat has ' + myCat['color'] + ' fur.'
print(line)

#-------------------------------------------------
# Order doesn't matter

myCat  = {'size': 'fat',
          'color': 'black',
          'sound': 'Meow'
         }

urCat  = {
          'color': 'black',
          'size': 'fat',
          'sound': 'Meow'
         }

print(myCat == urCat)

#--------------------------------------------------
# Existence

print('size' in myCat)
print('slim' in myCat.values())  # See values below

#--------------------------------------------------
# Methods

# keys method -------------------------------------
print(list(myCat.keys()))   # if !list,
                            #   returns dict_keys()

for k in myCat.keys():
    print(k)


# values methos ----------------------------------
print(list(myCat.values()))

for v in myCat.values():
    print(v)
 

# items method -----------------------------------
print(list(myCat.items()))  # return tuples

for i in myCat.items():
    print(i)

for k, v in myCat.items():
    print(k + ": " + v)

# get method ------------------------------------

if 'size' in myCat:
    print(myCat['size'])

# if in return, else 0
print(myCat.get('weight', 0))


# setdefault method -----------------------------

if 'weight' not in myCat:
    myCat['weight'] = '15 kg'

print(myCat)

# Alternative
myCat.setdefault('eyes', 'grey')  # only if !it 
print(myCat)


# ----------------------------------------------
# Note: 
# Tuples are immutable lists which use (), ![]