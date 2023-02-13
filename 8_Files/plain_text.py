msg = open('./8_Files/message.txt') # passing r does same

# Only reads text files not binaries
print(msg.read())

# Closing
msg.close()

# list of lines
msg = open('./8_Files/message.txt')
print(msg.readlines())       
msg.close()

# create or overwrite

# msg = open('./8_Files/nonsense.txt', 'w')
# msg.write('DBFHDSBVJH SDJHF DSJHVHDSVDSFLK\n')
# msg.write('DBFHDSBVJH SDJHF DSJHVHDSVDSFLK\n')
# msg.close()

# Appends
msg = open('./8_Files/nonsense.txt', 'a')
# msg.write('Does this work\n')
msg.close()


