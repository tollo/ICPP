# Find common divisors of two numbers
# Introduction to Compututation and Programming uising Python

d = {}
for x in 'ab':
    # Error handling for data types other than 'int'
    while True:
        try:
            input_value = int(input('Integer_' + str(x) + ': '))
            break
        except ValueError:
            print('Please enter only integers')
    d['Integer_{0}'.format(x)] = input_value


def findExtremeDivisors(n1, n2):
    """Assumes that n1 and n2 are positive integers
       Returns a tuple containing the smallest common divisor > 1
       and the largest common divisor of n1 and n2"""
#    divisors = ()  # the empty tuple
    minVal, maxVal = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            if minVal is None or i < minVal:
                minVal = i
            if maxVal is None or i > maxVal:
                maxVal = i
    return (minVal, maxVal)

minDivisor, maxDivisor = findExtremeDivisors(d['Integer_a'], d['Integer_b'])

print(minDivisor)
print(maxDivisor)


# def findDivisors(n1, n2):
#    """Assumes that n1 and n2 are positive integers
#       Returns a tuple containing all common divisors of n1 and n2"""
#    divisors = ()  # the empty tuple
#    for i in range(1, min(n1, n2) + 1):
#        if n1 % i == 0 and n2 % 1 == 0:
#            divisors = divisors + (i,)
#    return divisors
#
# divisors = findDivisors(20, 100)
# print(divisors)
# total = 0
# for d in divisors:
#    total += d
# print(total)
