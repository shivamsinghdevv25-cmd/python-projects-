import random
com= random.randint(1,100)
while True:
    num = int(input('guess a number between 1 to 100:'))
    if num == com:
        print('congratulations you won!!')
    elif num > com:
        print('your guess is high')
    elif num < com:
        print('your guess is low')