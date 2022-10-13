import time
#collatz sequence


#collatz function
def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1

starttime = time.time()
try:
    value = int(input("Enter a number: "))

    while value != 1:
        holder = collatz(value)
        print(holder)

        value = holder 

except ValueError:
    print("Error, wrong number.")

endtime = time.time()

print('Took %s seconds to calculate.' % (endtime - starttime))
