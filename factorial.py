# Print factorials


while True:
    try:
        input_value = int(input('Integer: '))
        break
    except ValueError:
        print('Please enter only integers')


def factI(n):
    """Assumes that n is an int > 0
       Returns n!"""
    result = 1
    while n > 1:
        result = result * n
        n -= 1
    return result


def factR(n):
    """Assumes that n is an int > 0
       Returns n!"""
    if n == 1:
        return n
    else:
        return n*factR(n - 1)

print(input_value, 'factorial is: ', factI(input_value))

print(input_value, 'factorial is: ', factR(input_value))
