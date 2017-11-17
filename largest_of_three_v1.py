# largest_of_three_v1.py
""" Compares three variables and returns the largest odd number of the three"""


def main():
    """ Main program"""

    print('Input three integers')

    # Create a dictionary to store values
    dict_list = {}
    for num in range(1, 4):
        # Error handling for data types other than 'int'
        while True:
            try:
                input_value = int(input('Integer_' + str(num) + ': '))
                break
            except ValueError:
                print('Please enter only integers')
        # Remove even numbers
        if input_value % 2 == 0:
            input_value = False
        # Populate dictionary
        dict_list['Integer_{0}'.format(num)] = input_value

    # Iterate and compare dictionary values
    largest_number = False
    for num in range(1, 4):
        if dict_list['Integer_{0}'.format(num)] > largest_number:
            largest_number = dict_list['Integer_{0}'.format(num)]

    if largest_number is False:
        print('No number is odd')
    else:
        print('The largest odd number entered is: ' + str(largest_number))

main()
