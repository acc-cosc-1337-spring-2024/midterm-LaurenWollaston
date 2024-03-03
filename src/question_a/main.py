import question_a

on = True
while on:
    print('')
    primeable = input("Enter a number to check if it is prime. If you would like to quit, type Quit or Q.:  ")
    if primeable.upper() == 'QUIT' or primeable.upper() == 'Q':
        on = False
    else:
        if not primeable or not primeable.isnumeric():
            print('Error')
        else:
            primeable = int(primeable)
            print(question_a.is_prime(primeable))
