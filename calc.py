import sys

line = input()
split = line.split()

first = int( split[0])
oper = split[1]
sec = int(split[2])

val = 0


if oper == '+':
	val = first + sec
elif oper == '-':
	val = first - sec
elif oper == '*':
	val = first * sec
elif oper == '/':
	if sec != 0:
		val = first / sec
	else:
		print('cannot divide by zero')
		sys.exit()
else:
	print('unknown operator: {op}'.format(op=oper))
	sys.exit()

print(val)