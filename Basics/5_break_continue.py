spam = 0
while spam < 10: 
    spam += 1
    if spam == 2:
        continue
    if spam == 9:
        break
    print('Spam is: ' + str(spam))
