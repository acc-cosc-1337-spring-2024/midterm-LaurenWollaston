import question_c
on = True
while on:
    print('')
    val = question_c.get_random_number()
    guess = input("Guess a number between 1 and 5. If you would like to quit, type Quit or Q.:  ")
    if guess.upper() == 'QUIT' or guess.upper() == 'Q':
        on = False
    else:
        if not guess or not guess.isnumeric():
            print('Error: Enter a number between 1 and 5.')
        else:
            if int(guess)>5 or int(guess)<1:
                print('Error: Enter a number between 1 and 5.')
            elif val == int(guess):
                print('Congratulations! You win!')
            else:
                print('Sorry, try again.')