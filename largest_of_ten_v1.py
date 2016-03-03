# Compares ten variables and returns the largest odd number of the ten

def program():

    print('Input ten integers')

   # Create a dictionary to store values
    d = {}
    for x in range(1,11):
        # Error handling for data types other than 'int'
        while True:
            try:
                input_value = int(input('Integer_' + str(x) + ': '))
                break
            except ValueError:
                print('Please enter only integers')
        # Remove even numbers
        if (input_value %2 == 0):
            input_value = False
        # Populate dictionary
        d['Integer_{0}'.format(x)]=input_value

    # Iterate and compare dictionary values
    largest_number = False
    for x in range(1,11):
        if d['Integer_{0}'.format(x)] > largest_number:
            largest_number = d['Integer_{0}'.format(x)]

    if largest_number == False:
        print('No number is odd')
    else:
        print('The largest odd number entered is: ' + str(largest_number))

program()
