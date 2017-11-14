# find_root.py
""" Find the root of a number
    Example from Intoduction to Computation and Programming using Python"""


def find_root(find_x, power, epsilon):
    """Assumes x and epsilon in or float, power an int,
           epsilon > 0 & power >= 1
       Returns float y such that y**power is within epsilon of x.
           If such a float does not exist, it returns None"""
    if find_x < 0 and power % 2 == 0:
        return None
    low = min(-1.0, find_x)
    high = max(1.0, find_x)
    ans = (high + low) / 2.0
    while abs(ans**power - find_x) >= epsilon:
        if ans**power < find_x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    return ans


def test_find_root():
    """ Test function"""
    epsilon = 0.0001
    for test_x in (0.25, -0.25, 2, -2, 8, -8):
        for power in range(1, 4):
            print('Testing x = ' + str(test_x) +
                  ' and power = ' + str(power))
            result = find_root(test_x, power, epsilon)
            if result is None:
                print('     No root')
            else:
                print('    ', result, '**', power, '~+', test_x)

def main():
    """ Main function"""
    test_find_root()

main()
