from random import randint

rollAgain = True

while rollAgain: 

	die_one = randint(1, 6)

	die_two = randint(1, 6)

	print('\nNow we have {d1}! and {d2}!!\n'.format(d1 = die_one, d2 = die_two))

	command = str(input('y for yes | n for no\n'))
		
	if command == 'y':
		rollAgain = True
	else:
		rollAgain = False
		if command != 'n':
			print('enter only y or n')
