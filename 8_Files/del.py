import os

# os.unlink('8_Files/dat')

# Remove Directory (empty folders)
# os.rmdir()

import shutil

# Deletes folders and files  
# shutil.rmtree()

os.chdir('8_Files')
for filename in os.listdir():
    if filename.endswith('.txt'): 
        # os.unlink(filename)
        print(filename)

# Send to Trash
import send2trash

send2trash.send2trash('dat')