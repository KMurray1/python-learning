import random

random_number = random.randint(1,100)
guess = None


while guess != random_number:
    guess = int(input('Guess number: '))
    if guess > random_number:
        print('Too high bruh!')
    elif guess < random_number:
        print('Too low')
    else:
        print('You got it!')