# Introduction to Computing and Programming using Python


def findAnEven(l):
    """Assumes l is a list of integers
       Returns the first even number in l
       Raises ValueError if l does not contain an even number"""

    for i in l:
        if i % 2 == 0:
            print('First even number in list is: ', i)
            break
    else:
        raise ValueError('list contains no even numbers')

findAnEven([1, 5, 3, 7, 5])
