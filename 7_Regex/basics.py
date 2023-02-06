# US phone number
# Without regex: Not gonna try XD
# I think regex is const: minilang

import re

message = 'Her number is 123-456-7890, maybe 987-654-3210. Try yourself.'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # as regex uses \

mo = phoneNumRegex.findall(message)    # match object
print(mo)

# for single .search, then mo.group