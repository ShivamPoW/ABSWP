import re

str = 'Agent Nostr oranged pill Agent Twitter'

# Sub method 
namesRegex = re.compile(r'Agent (\w+)')
print(namesRegex.findall(str))

print(namesRegex.sub('REDACTED', str)) #Finds and Substitutes


# Sub method (grps)
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall(str))

print(namesRegex.sub(r'Agent \1****', str))

