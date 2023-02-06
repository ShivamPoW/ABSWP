# Upper

str = "Chancellor on the Brink of Second Bailout for Banks"

print(str.upper())
print(str.lower())


#----------
# UseCase

# answer = input()
# if answer.lower() == 'yes':
#     print('Well Done')
#     print(answer.islower())

#------------
# isalph() : letter only
# isalnum() : letter and numbers only
# isdecimal() : numbers only
# isspace() : whitespace only
# istitle() : titlecase only

print('123'.isdecimal())
print('123isawu'.isalnum())
print('  d   '.isspace())
print('Hi There Bro'.istitle())

#----------
# startswith, endswith, join

print('Hi there'.startswith('Hi'))
print('Hi there'.endswith('.'))
print(' '.join(['Hi', 'there', 'bero']))
print('\n'.join(['Hi', 'there', 'bero']))

#---------
# split

print('My name is Hehe'.split())
print('My name is Hehe'.split('m'))

#---------
# ljust(): left, char right
# rjust(): right, char left
# center
 
print(str.rjust(70))
print(str.ljust(70))
print(str.ljust(70,'-'))
print(str.center(70,'='))


#--------
# strip(), rstrip(), lstrip()

str1 = '           Hello         '
str2 = 'lalallllllllHellollllllallll'
print(str1.strip())
print(str1.rstrip())
print(str2.strip('la'))

#------- 
# replace

spam = 'color'
print(spam.replace('o', 'ou'))
