prompt = 'Give me a number:\n>>> '
number = float(input(prompt))

if number % 10 == 0:
    print('\n' + str(int(number)) + ' is a multiple of 10')
else:
    print('\n' + str(int(number)) + ' is NOT a multiple of 10')