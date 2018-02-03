from random import randint

goal = randint(1, 99)
user_guess = 0
turns = 0

print("\nHi! Lets play a game\nI'm thinking of a number between 1 - 99\n")

while goal != user_guess:
	user_guess = int(input('\n'))
	turns +=1
	
	if user_guess < goal:
		print('\nNope, try higher')
	elif user_guess > goal:
		print('\nNope, try less')
	if user_guess == goal:
		print('\nwoaaaaah, way to go')
		print('\nYou did that in {t} turn(s)'.format(t = turns))
