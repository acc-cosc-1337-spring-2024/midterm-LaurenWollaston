import question_b
on = True
while on:
    print('')
    val = input("Enter a number 1 - 7 to see its corresponding day of the week. If you would like to quit, type Quit or Q.:  ")
    if val.upper() == 'QUIT' or val.upper() == 'Q':
        on = False
    else:
        print(question_b.get_day_of_week(val))
