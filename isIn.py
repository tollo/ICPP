# Take two strings and see if either is in the other


while True:
    try:
        string_1 = str(input('String 1: '))
        break
    except ValueError:
        print('Please enter a string')

while True:
    try:
        string_2 = str(input('String 2: '))
        break
    except ValueError:
        print('Please enter a string')

if string_1 in string_2 or string_2 in string_1:
    print('True')
else:
    print('False')
