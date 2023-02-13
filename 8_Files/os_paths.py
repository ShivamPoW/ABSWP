import os          

# Rel: Relative,  Abs: Absolute
# Here I'm mostly using Rel PATH but Abs works!
# Here Dir = Main 

# path depending upon OS
PATH = os.path.join('home','bitcoin','test')

print(PATH)

# Get Seprator
print(os.sep)

# current working directory
print(os.getcwd())

# To change working dir:  
# print(os.chdir('./8_Files'))

# Rel/Abs PATH
# .  : This Folder |  .. : Parent Folder

print(os.path.isabs('absolute_relative_paths.py'))         # Checks if Abs PATH
print(os.path.abspath('absolute_relative_paths.py'))       # Return abs PATH
print(os.path.abspath('../../absolute_relative_paths.py')) # Rel to Abs conversion


# Get Relative PATH
relPATH = os.path.relpath('3_Error_&_Program/try_except.py','absolute_relative_paths.py')
print(relPATH)


# Directory PATH and Basename (Last Part)
PATH = '/home/<YOUR_PC>/Desktop/CS/ABSWP/7_Regex/Project/phone_email.py'

dirName = os.path.dirname(PATH)
baseName = os.path.basename(PATH)
print(dirName)
print(baseName)


# Check if File exists (exists, isfile, isdir)
BOOL = os.path.exists('5_Dictionaries/tic_tac_toe.py')
print(BOOL)

BOOL = os.path.isfile('5_Dictionaries/tic_tac_toe.py')
print(BOOL)

BOOL = os.path.isdir('5_Dictionaries/tic_tac_toe.py')
print(BOOL)


# get File Size in Bytes
SIZE = os.path.getsize('3_Error_&_Program/guess.py')
print(SIZE)

# List of files and Folders
LIST = os.listdir('./')
print(LIST)

## Small Program
# Finds sum of size of all files in a folder

totalSize = 0
for filename in os.listdir('./'):            # . does same
    if not os.path.isfile(filename):         # for Abs: os.path.join('dirname', filename)
        continue
    totalSize += os.path.getsize(filename)

print(totalSize)


# Make directories
# os.makedirs('./Test/PASSED')                 # / giving me [Errno 13] Permission Denied

