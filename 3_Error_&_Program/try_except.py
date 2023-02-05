def div100by(divideBy):
    try:
        return 100 / divideBy
    except ZeroDivisionError:                 # except accepts all
        return 'ERR: Don\'t waste my time'


print(div100by(0))
print(div100by(100))

# ----------------------------------------------------
print()



print('Type Fav Number: ')
num = input()

try: 
    if int(num) >= 100:
        print('Big')
    elif int(num) < 100: 
        print('Small')
except:
    print('Why did you did this!')