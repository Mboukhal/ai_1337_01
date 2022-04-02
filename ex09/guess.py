#!/usr/bin/env python

from random import randint

if __name__ == '__main__':

    print("This is an interactive guessing game!\
        \nYou have to enter a number between 1 and 99 to find out the secret number.\
        \nType 'exit' to end the game.\
        \nGood luck!\n")
    number = randint(1, 99)
    user = 0
    exit_user = ''
    i = 0

    while True:

        print('What\'s your guess between 1 and 99?')
        user = input('>> ')
        i += 1

        if user == 'exit':
            print('Goodbye!')
            exit(0)
        elif (not user.isnumeric()) and user != 'exit':
            print('That\'s not a number.')
        elif int(user) < number:
            print('Too low!')
        elif int(user) > number:
            print('Too high!')
        elif int(user) == number and i == 1:
            print("The answer to the ultimate question of life, the universe and everything is 42.\
                \nCongratulations! You got it on your first try!")
            exit(0)
        elif int(user) == number:
            print(f'Congratulations, you\'ve got it! \
                \nYou won in {i} attempts!')
            exit(0)