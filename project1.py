import random

def guess_number():
    comp_number = random.randint(1,5)
    attempts = 0

     
    wrong_guess = True
    while wrong_guess:
        guess = int(input('enter guessed number between 1 and 5: '))
        attempts = attempts +1

        if guess < comp_number:
            print('number is too low, Try again!')
        elif guess > comp_number:
            print('number is too high, Try again!')
        else:
            print(f"you guessed the number in {attempts} attempts ")
            wrong_guess = False

    print("Game finished")

guess_number()

