import random


value = int(input('''Enter the length of the password
It should not be greter than 7 characters: '''))

bank = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '<', '?', '/', '>','1', '2', '3', '4', '5', '6', '7', '8', '9', '0','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

i=0
array = []

if value >= 7:
    while i != value:
        choice = random.choice(bank)

        array.append(choice)
        i+=1
else:
    print("Hey it's too short. Choose something longer!")

for j in array:
    final_password = j

print(final_password)

# with open('password.txt', 'w') as document:
#     document.write(j)
    


# print('Done and Dusted Man')