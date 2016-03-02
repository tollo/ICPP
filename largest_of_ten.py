# Compares ten variables and returns the largest of the ten


def program():

    print('Input ten integers')

    # Error handling for numbers other than integers input
    while True:
        try:
            N1 = int(input('N1: '))
            break
        except ValueError:
            print('Please enter only integers')

    while True:
        try:
            N2 = int(input('N2: '))
            break
        except ValueError:
            print('Please enter only integers')

    while True:
        try:
            N3 = int(input('N3: '))
            break
        except ValueError:
            print('Please enter only integers')

    while True:
        try:
            N4 = int(input('N4: '))
            break
        except ValueError:
            print('Please enter only integers')

    while True:
        try:
            N5 = int(input('N5: '))
            break
        except ValueError:
            print('Please enter only integers')

    while True:
        try:
            N6 = int(input('N6: '))
            break
        except ValueError:
            print('Please enter only integers')

    while True:
        try:
            N7 = int(input('N7: '))
            break
        except ValueError:
            print('Please enter only integers')

    while True:
        try:
            N8 = int(input('N8: '))
            break
        except ValueError:
            print('Please enter only integers')

    while True:
        try:
            N9 = int(input('N9: '))
            break
        except ValueError:
            print('Please enter only integers')

    while True:
        try:
            N10 = int(input('N10: '))
            break
        except ValueError:
            print('Please enter only integers')

    # Retaining only odd numbers
    if (N1%2 != 0) or (N1 == 1):
        N1 = N1
    else:
        N1 = -99999999999999999999

    if (N2%2 != 0) or (N2 == 1):
        N2 = N2
    else:
        N2 = -99999999999999999999

    if (N3%2 != 0) or (N3 == 1):
        N3 = N3
    else:
        N3 = -99999999999999999999

    if (N4%2 != 0) or (N4 == 1):
        N4 = N4
    else:
        N4 = -99999999999999999999

    if (N5%2 != 0) or (N5 == 1):
        N5 = N5
    else:
        N5 = -99999999999999999999

    if (N6%2 != 0) or (N6 == 1):
        N6 = N6
    else:
        N6 = -99999999999999999999

    if (N7%2 != 0) or (N7 == 1):
        N7 = N7
    else:
        N7 = -99999999999999999999

    if (N8%2 != 0) or (N8 == 1):
        N8 = N8
    else:
        N8 = -99999999999999999999

    if (N9%2 != 0) or (N9 == 1):
        N9 = N9
    else:
        N9 = -99999999999999999999

    if (N10%2 != 0) or (N10 == 1):
        N10 = N10
    else:
        N10 = -99999999999999999999

    if (N1 > N2 and N1 > N3 and N1 > N4 and N1 > N5 and N1 > N6 and N1 > N7
            and N1 > N8 and N1 > N9 and N1 > N10):
        print('N1 (' + str(N1) + ') is the largest odd number')
    elif (N2 > N3 and N2 > N4 and N2 > N5 and N2 > N6 and N2 > N7 and N2 > N8
            and N2 > N9 and N2 > N10):
        print('N2 (' + str(N2) + ') is the largest odd number')
    elif (N3 > N4 and N3 > N5 and N3 > N6 and N3 > N7 and N3 > N8 and N3 > N9
            and N3 > N10):
        print('N3 (' + str(N3) + ') is the largest odd number')
    elif (N4 > N5 and N4 > N6 and N4 > N7 and N4 > N8 and N4 > N9
            and N4 > N10):
        print('N4 (' + str(N4) + ') is the largest odd number')
    elif (N5 > N6 and N5 > N7 and N5 > N8 and N5 > N9 and N5 > N10):
        print('N5 (' + str(N5) + ') is the largest odd number')
    elif (N6 > N7 and N6 > N8 and N6 > N9 and N6 > N10):
        print('N6 (' + str(N6) + ') is the largest odd number')
    elif (N7 > N8 and N7 > N9 and N7 > N10):
        print('N7 (' + str(N7) + ') is the largest odd number')
    elif (N8 > N9 and N8 > N10):
        print('N8 (' + str(N8) + ') is the largest odd number')
    elif (N9 > N10):
        print('N9 (' + str(N9) + ') is the largest odd number')
    elif (N10 != -99999999999999999999):
        print('N10 (' + str(N10) + ') is the largest odd number')
    else:
        print('No number is odd!')

program()


