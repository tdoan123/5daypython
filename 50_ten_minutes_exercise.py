'''
Exercise 1: Number guessing game 
For this exercise
- Write a function (guessing_game) that takes no arguments.
- When run, the function chooses a random integer between 0 and 100 (inclusive).
Then ask the user to guess what number has been chosen.
- Each time the user enters a guess, the program indicates one of the following:
- Too high/ Too low/ Just right
- If the user guesses correctly, the program exits. Otherwise, the user is asked to
try again.
- The program only exits after the user guesses correctly.
'''

import random

def guessing_name():
    answer = random.randint(0,100)
    print (answer)
    
    while True: 
        user_guess = int(input('what is your guess? ' ))
        
        if user_guess == answer: 
            print(f'Binggo, the answer is {answer}')
            break 
        
        if user_guess < answer: 
            print(f'Your guess of {user_guess} is lower than the answer')
        
        else:  
            print(f'Your guess of {user_guess} is higher than the answer')

guessing_name()

### today, try different scenarios 1) guess words, 2) providing hint for user response thus they can do better guess 


