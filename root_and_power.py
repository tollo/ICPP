# Express a number as a root and power

while True:
    try:
        x = int(input('Enter an Integer: '))
        break
    except ValueError:
        print('Please enter only integers')

for root in range(2,abs(x)):
    pwr = 0
    while root**pwr < abs(x):
        pwr = pwr + 1
    if root**pwr == abs(x):
        break

if root**pwr != abs(x):
    print(x, 'is not a perfect power')
else:
    if x < 0 and pwr%2 != 1:
        print('Imaginary Number')
    elif x < 0:
        root = -root
        print(root, 'to the power of', pwr, 'is', x)
    else:
        print(root, 'to the power of', pwr, 'is', x)

