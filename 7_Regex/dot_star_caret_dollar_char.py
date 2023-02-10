# ^ : Begining (caret)
# $ : End


import re

str = 'Time is Money!'

one = re.compile(r'^Time')
two = re.compile(r'Money!$')
three = re.compile(r'^\d+$')

print(one.search(str).group())
print(two.search(str).group())
print(three.search(str))

# . : Any char except newline

four = re.compile(r'.e')
print(four.findall(str))  # notice me NOT Time

four = re.compile(r'.{2,3}e')    # two-three char (use *)
print(four.findall(str))

# .* are used togeher

str = 'First Name: Satoshi Last Name: Nakamoto'                  #for one search 
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')      #Greedy 
nameRegex = re.compile(r'First Name: (.*?) Last Name: (.*?)')    #Non Greedy
print(nameRegex.findall(str))

# Greedy / Non Greedy

str = '(It\'s time) Humans)'
ng = re.compile(r"\((.*?)\)")
g = re.compile(r"\((.*)\)")

print(ng.search(str).group())  # Non Greedy
print(g.findall(str))   # Greedy

# . exception (newline\)

str = 'I \nknew it \nlong ago'

print(re.compile(r'.*').search(str).group())

# Selecting everything

ev = re.compile(r'.*',re.DOTALL)
print(ev.search(str).group())

# Ignoring case

cs = re.compile(r'[aeiou]', re.I)  # re.I = re.IGNORECASE
print(cs.findall(str))

