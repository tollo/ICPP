# fibonacci.py
""" Prints the fibonacci number of an input integer
    Uses global variables
    Uses a test program to test the number of program calls"""

# Defining global variable to use across functions
NUM_FIB_CALLS = 0


def fib(input_integer):
    """ Assumes that input_integer is an int > 0
        Returns Fibonacci of input_integer"""
    global NUM_FIB_CALLS
    NUM_FIB_CALLS += 1
    if input_integer == 0 or input_integer == 1:
        return 1
    return fib(input_integer-1) + fib(input_integer-2)


def test_fib(input_integer):
    """Test program for fib"""
    for i in range(input_integer+1):
        global NUM_FIB_CALLS
        NUM_FIB_CALLS = 0
        print('fib of ', i, '=', fib(i))
        print('fib called', NUM_FIB_CALLS, 'times')


def main():
    """Main program"""
    while True:
        try:
            input_value = int(input('Integer: '))
            break
        except ValueError:
            print('Please enter only integers')
    test_fib(input_value)


main()
