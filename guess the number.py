import random
com= random.randint(1,100)
tries = 0
while True:
    tries+=1
    num = int(input('guess a number between 1 to 100:'))
    if num == com:
        print('congratulations you won!!')
    elif num > com:
        print('your guess is high')
    elif num < com:
        print('your guess is low')
