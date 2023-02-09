# \d     :    0-9
# \D     :   !0-9
# \w     :    0-9,A-Z,a-z,_
# \W     :    !\w
# \s     :    space, tab, newline
# \S     :    \s

# I think there are lot more

import re

lyrics = '1 space123, 1 universe213, 1 galaxy, 1 planet, 1 continent, 1 country, 1 state, 1 city and 1 sq feet of land'

lRegex = re.compile(r'\d+\s\w+')

print(lRegex.findall(lyrics))

# create char class 
# [], Range: [-], Negation [^]

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall(lyrics))

# better way of doing first

lRegex = re.compile(r'\d+\s[a-zA-Z]+')
print(lRegex.findall(lyrics))

# Negation example
noVowelRegex = re.compile(r'[^aeiouAEIOU]')
print(noVowelRegex.findall(lyrics))

