# Escape Charcters/Sequence
# \' \" \t \n \\

print('His mobile\'s OS')   # esc req

print("His mobile's \n\t\tOS")

print("His mobile's \n\t\t\b\b\bOS")


# Raw strings
print(r'Hello there\, World is Doomed!')

# Multilines with ''' / """

spam = '''Why? 
Why not, 
It's the 
Dark age.'''

print(spam)

# ------------------------------------------
# list similarity

print('\n' + spam[0])
print(spam[-1])
print('Why' in spam)