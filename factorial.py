# factorial.py
"""Prints the factorial of an integer twice:
    once using iteration,
    and a second time using recursion"""


def fact_i(input_integer):
    """Assumes that input_integer is an int > 0
       Returns n!"""
    result = 1
    while input_integer > 1:
        result = result * input_integer
        input_integer -= 1
    return result


def fact_r(input_integer):
    """Assumes that input_integer is an int > 0
       Returns n!"""
    if input_integer == 1:
        return input_integer
    return input_integer*fact_r(input_integer - 1)


def main():
    """Main program"""
    while True:
        try:
            input_value = int(input('Integer: '))
            break
        except ValueError:
            print('Please enter only integers')
    print(input_value, 'factorial is: ', fact_i(input_value))
    print(input_value, 'factorial is: ', fact_r(input_value))


main()
