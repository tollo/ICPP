# Introduction to Computing and Programming using Python


def sumDigits(s):
    """Assumes s is a string
       Returns the sum of the decimal digits in s
       For example, if s is 'a2b3c' it returns 5"""
    total = 0
    for i in s:
        try:
            i = int(i)
        except ValueError:
            i = 0
        total = total + i
    return(total)

string = input('Enter a string: ')

print(sumDigits(string))
