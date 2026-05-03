numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] #array for numbers

for number in numbers: #simple loop that first checks if the number is even or odd, then prints the relevant statement
    if (number % 2 == 0):
        print(str(number) + " is even.")
    else:
        print(str(number) + " is odd.")
#str function used because otherwise it doesn't let me concatenate an int and a string
