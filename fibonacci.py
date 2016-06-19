# Print fibonacci number


while True:
    try:
        input_value = int(input('Integer: '))
        break
    except ValueError:
        print('Please enter only integers')


def fib(n):
    """Assumes that n is an int > 0
       Returns Fibonacci of n"""
    global numFibCalls
    numFibCalls += 1
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def testFib(n):
    for i in range(n+1):
        global numFibCalls
        numFibCalls = 0
        print('fib of ', i, '=', fib(i))
        print('fib called', numFibCalls, 'times')


testFib(input_value)