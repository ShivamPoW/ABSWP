import re

str = '123-123-123, 321-321-321'

# Comment in Regexs

regx = re.compile(r'''
(\d{3})    # Bla Bla Bla
-
(\d{3})    # Lab Lab Lab
-
(\d{3})    # Abl Abl Abl
''', re.VERBOSE)

print(regx.findall(str))

# Note > To use re.I, re.VERBOSE just use :
# | bitwise operator