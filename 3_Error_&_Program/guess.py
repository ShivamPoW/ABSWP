import random
print('Hello, What\'s your name pleb') 
name = input()
myNum = random.randint(1,21)
print('Well ' + name + ', I know a secret number between 1 and 20.')

for i in range(1,7): 
    print('Make a guess.')
    num = int(input())
    if num > myNum: 
        print('Your guess is too high.')
    elif num < myNum: 
        print('Your guess is too low.')
    else:
        print('Good Job! '+ name + ', Right Guess!')
        print('You took ' + str(i) + ' guesses!')
        break
if num != myNum:
    print('Nope. I was thinking of ' + str(myNum))