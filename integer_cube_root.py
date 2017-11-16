# integer_cube_root.py
""" Find the cube root of an integer by exhaustive enumeration
    Example from Introduction to Computing and Programming using Python"""

def main():
    """ Main program"""

    while True:
        try:
            input_value = int(input('Enter an integer: '))
            break
        except ValueError:
            print('Please enter only integers')

    ans = 0

    while ans**3 < abs(input_value):
        ans = ans + 1

    if ans**3 != abs(input_value):
        print(input_value, 'is not a perfect cube')

    else:
        if input_value < 0:
            ans = -ans
        print('Cube root of', input_value, 'is', ans)


main()
