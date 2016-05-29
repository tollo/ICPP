# Cube root using bisection search
# Introduction to Computation and Programming Using Python


while True:
    try:
        input_value = int(input('Integer: '))
        break
    except ValueError:
        print('Please enter only integers')

x = abs(input_value)
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans**3 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('numGuesses =', numGuesses)
if input_value < 0:
    ans = - ans
print(ans, 'is close to square root of', x)
