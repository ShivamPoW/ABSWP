import os, shutil

os.chdir('8_Files')

for folderName,SubFolders, File  in os.walk('Sample'):
    print('The Folder is: ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(SubFolders))
    print('The files in ' + folderName + ' are: ' + str(File))
    print()             # or Just add '\n' but ig it's non-pythonic

    for subfolder in SubFolders:
        if subfolder.endswith('am'):
            print(subfolder)
            # os.rmdir(subfolder)    # why err

    for file in File:
        if file.endswith('.txt'):
            print(file)  # rename, whatever u want
            # shutil.move(os.path.join(folderName, file), os.path.join(folderName, file + '.xyz'))
    

