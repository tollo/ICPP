# square_an_integer.py
""" Square an integer the long way"""

def main():
    """ Main program"""

    while True:
        try:
            input_value = int(input('Please enter an integer: '))
            break
        except ValueError:
            print('Please enter only integers')
    ans = 0
    iters_left = abs(input_value)
    while iters_left != 0:
        ans = ans + abs(input_value)
        iters_left = iters_left - 1
    print(str(input_value) + '*' + str(input_value) + ' = ' + str(ans))


main()
