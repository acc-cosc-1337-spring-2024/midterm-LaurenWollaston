import question_d
print('')
print('+----------+----------+')
print('| Celcius  |Fahrenheit|')
print('+----------+----------+')
for i in range (0, 21):
    print('|   '+str(i).zfill(2)+'     |    '+str(int(question_d.getFahrenheit(i))).zfill(2)+'    |')
    print('+----------+----------+')