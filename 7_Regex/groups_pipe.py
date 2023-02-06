import re

message = 'Her number is 123-456-7890, maybe 987-654-3210. Try yourself.'
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d\-\d\d\d\d)') 

# Groups

mo = phoneNumRegex.search(message)
print(mo.group(1))
print(mo.group(2))

# if literall looking for () use \

message = 'Her number is (123) (456 7890), maybe (987) (654 3210). Try yourself.'
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\(\d\d\d \d\d\d\d\))') 

mo = phoneNumRegex.search(message)
print(mo.group(1))
print(mo.group(2))

# Pipe character | i.e above ENTER

batRegex = re.compile(r'Bat(man|mobile|copter)')  # Not a DC fan
mo = batRegex.search('Batman riding Batmobile')

print(mo.group())
print(mo.group(1))
print(batRegex.findall('Batman riding Batmobile'))  # Weird (look ./findall.py)