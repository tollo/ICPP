# Compares three variables and returns the largest of the three


def program():

    # Check to see if the numbers input are valid
    def checkval (a):
        if a < 0:
            print('Numbers must be positive!')
        elif a == 0:
            print('Numbers cannot be 0')
        elif a == 1:
            print('Number must be greater than 1')
        else:
            return('OK')

    print('Input a positive integer greater than 1')

    # Error handling for numbers other than integers input
    while True:
        try:
            x = int(input('x: '))
            if checkval(x) == 'OK':
                break
        except ValueError:
            print('Please enter only integers')

    while True:
        try:
            y = int(input('y: '))
            if checkval(y) == 'OK':
                break
        except ValueError:
            print('Please enter only integers')

    while True:
        try:
            z = int(input('z: '))
            if checkval(z) == 'OK':
                break
        except ValueError:
            print('Please enter only integers')

    # Retaining only odd numbers
    if (x%2 != 0):
        x = x
    else:
        x = 0
    if (y%2 != 0):
        y = y
    else:
        y = 0
    if (z%2 != 0):
        z = z
    else:
        z = 0

    if x > y and x > z:
        print('x (' + str(x) + ') is the largest odd number')
    elif y > z:
        print('y (' + str(y) + ') is the largest odd number')
    elif z != 0:
        print('z (' + str(z) + ') is the largest odd number')
    else:
        print('No number is odd!')


program()


