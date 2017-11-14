# cube_root_bisection.py
""" Find cube root using bisection search
    Excercise from Introduction to Computation and Programming Using Python"""

def main():
    """ Main program"""
    while True:
        try:
            input_value = int(input('Integer: '))
            break
        except ValueError:
            print('Please enter only integers')

    abs_val_input = abs(input_value)
    epsilon = 0.01
    num_guesses = 0
    low = 0.0
    high = max(1.0, abs_val_input)
    ans = (high + low) / 2.0
    while abs(ans**3 - abs_val_input) >= epsilon:
        print('low =', low, 'high =', high, 'ans =', ans)
        num_guesses += 1
        if ans**3 < abs_val_input:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    print('num_guesses =', num_guesses)
    if input_value < 0:
        ans = - ans
    print(ans, 'is close to square root of', abs_val_input)


main()
