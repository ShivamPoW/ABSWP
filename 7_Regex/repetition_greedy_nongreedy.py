import re

# ? char -------------------------------------------
# 1 or 0 times

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The story of Batwoman')

print(mo.group())

# Making areacode optional -------------------------

import re

message = 'Her number is 456-7890, maybe 987-654-3210. Try yourself.'
phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') 

print(phoneNumRegex.search(message).group())

# * char --------------------------------------------
# any number of times [to escape use \]


batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The story of Batwowoman')

print(mo.group())

# + char --------------------------------------------
# 1 or more

batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The story of Batwowowowoman')

print(mo.group())
try: 
    mo1 = batRegex.search('The story of Batman')
    print(mo1.group())
except: 
    print('Not found')

# escaping --------------------------------------------

str = 'I learnt ?*+ regex syntax'
Regex = re.compile(r'\?\*\+')

print(Regex.search(str).group() == '?*+')

# { }, {,}-------------------------------------------------
# fix and range number of times

XDRegex = re.compile(r'(XD){3}')
print(XDRegex.search('XD XDXD XDXDXD').group())


XDRegex = re.compile(r'(XD){1,3}')
print(XDRegex.findall('XDXDXD XDXD XD')) # why XD not XDXDXD?
                                         #  look ./findall.py

# --------------------------------------------------------
# Re do greedy matches : 
#                        Initial and Longest (AND)

XDRegex = re.compile(r'(XD){1,3}')
print(XDRegex.search('XDXD XDXDXDXDXD').group())
print(XDRegex.search('XDXDXDXD XDXDXD').group())

#---------------------------------------------------------
# ? : No greedy Matches (shortest)

XDRegex = re.compile(r'(XD){1,3}?')
print(XDRegex.search('XDXD XDXDXDXDXD').group())
print(XDRegex.search('XDXDXDXD XDXDXD').group())