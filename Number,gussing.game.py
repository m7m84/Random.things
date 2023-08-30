import random
def number_guessing_game():
    lower_limit = 1
    upper_limit = 100
    secret_number = random.randint(lower_limit, upper_limit)
    guesses = 0
    while True :
        user_guess = int(input(f'guess a number between {lower_limit} and {upper_limit}'))
        guesses += 1
        if user_guess == secret_number :
            print('good job')
        elif user_guess < secret_number:
            print('try a bigger number')
        else :
            print('try a smaller number')
if __name__ =="__main__" :
    number_guessing_game()

