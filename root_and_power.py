# Express a number as a root and power

x = int(input('Enter an integer: '))

pwr = 6

ans = 0

while ans**pwr < abs(x):
    ans = ans + 1

if ans**pwr != abs(x):
    #decrement pwr here - but how to stop it? for loop?
    print(x, 'is not a perfect power of 1-6')
else:
    if x < 0:
        ans = -ans
    print(ans, 'to the power of', pwr, 'is', x)

