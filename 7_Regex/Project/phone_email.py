#! python3

import re
import pyperclip   # needs manual installation

# Regex for phone numbers, valid types: 
# 324-343-1223, 343-1213, (213) 342-2342, 213-2312 ext 12343, ext. 12345, x12343

phoneRegex = re.compile(r''' 
(
(\d{3}| \(\d{3}\))?     # Area code (optional)
(\s|-)                  # Sperator
\d{3}                   # first three digits
-                       # seprator
\d{4}                   # last four digits
((ext(\.)?\s|x)         # extenstion word-part (optional)
(\d{2,5}))?             # extension number-part (optional)
)
''' , re.VERBOSE)

# Email Regex

emailRegex = re.compile(r'''
# some.+_xyz@some.+_xyz.com
[a-zA-Z0-9_.+]+          # name part
@                        # @ symbol
[a-zA-Z0-9_.+]+          # domain part (ome.+_xyz.com)
\.                       # .
\w+                      # xcsd
''', re.VERBOSE)

# Get text from clipboard
text = pyperclip.paste()

# extract email/phone from text
extractPhone = phoneRegex.findall(text)
extractEmail = emailRegex.findall(text)

for number in extractPhone: 
    print(number[0],'\n')

print('\n'.join(extractEmail))
