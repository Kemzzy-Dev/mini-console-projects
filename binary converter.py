import math

number = int(input('Enter a binary or base 10 number: '))

while number != 0:
	remainder = number % 2
	answer = math.floor(number/2)
	number = answer
	print(remainder)