import time

#loop for the cipher
while True:
	#Letters to loop from and get the index
	letters = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
	 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c']

	#user input
	print('Enter /// to EXIT the program')
	user_input = input('Enter the text to be deciphered: ')
	#convert user input to lower text
	user_input.lower()

	#loop to get the user input
	for info in user_input:
		test = info in letters #testing to see if the user input is valid
		if test == True:
			cipher = (letters.index(info) - 3) #Moving the letters three times forward
			print(letters[cipher])#final result


	#To close the loop
	if user_input == '///':
		print('CLOSING........')
		time.sleep(1)
		print('Closed.')
		break