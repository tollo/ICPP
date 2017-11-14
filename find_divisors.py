# find_divisors.py
""" Find common divisors of two numbers
    Exercises from Introduction to Compututation and Programming uising Python"""


def main():
    """ Main function"""
    dict_list = {}
    for num in 'ab':
        # Error handling for data types other than 'int'
        while True:
            try:
                input_value = int(input('Integer_' + str(num) + ': '))
                break
            except ValueError:
                print('Please enter only integers')
        dict_list['Integer_{0}'.format(num)] = input_value


    def find_divisors(n_1, n_2):
        """Assumes that n1 and n2 are positive integers
        Returns a tuple containing all common divisors of n1 and n2"""
        divisors = ()  # the empty tuple
        for i in range(1, min(n_1, n_2) + 1):
            if n_1 % i == 0 and n_2 % 1 == 0:
                divisors = divisors + (i,)
        return divisors

    divisors = find_divisors(dict_list['Integer_a'], dict_list['Integer_b'])
    print(divisors)
    total = 0
    for _d_ in divisors:
        total += _d_
    print(total)

main()

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
