number = int(input('Enter your balance: '))
correct_number = '{:,}'.format(number)
print('Your updated balance: ${0} '.format(correct_number))