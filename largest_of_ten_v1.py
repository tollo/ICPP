# largest_of_ten_v1.py
""" Compares ten variables and returns the largest odd number of the ten"""


def main():
    """ Main program"""

    print('Input ten integers')

    # Create a dictionary to store values
    dict_list = {}
    for num in range(1, 11):
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
    for num in range(1, 11):
        if dict_list['Integer_{0}'.format(num)] > largest_number:
            largest_number = dict_list['Integer_{0}'.format(num)]

    if largest_number is False:
        print('No number is odd')
    else:
        print('The largest odd number entered is: ' + str(largest_number))

main()
