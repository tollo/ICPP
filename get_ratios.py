# Introduction to Computing and Programming using Python


def getRatios(vect1, vect2):
    """Assumes: vect1 and vect2 are lists of equal length of numbers
       Returns: a list containing the meaningful valvues of
                vect1[i]/vect2[i]"""

    ratios = []
    for index in range(len(vect1)):
        # print('New iteration')
        # print(index)
        try:
            ratios.append(vect1[index]/float(vect2[index]))
            # print(ratios)
        except ZeroDivisionError:
            ratios.append(float('nan'))  # nan = Not a Number
        except:
            raise ValueError('getRatios called with bad arguments')
    return ratios

try:
    print(getRatios([1.0, 2.0, 7.0, 6.0], [1.0, 2.0, 0.0, 3.0]))
    print(getRatios([], []))
    print(getRatios([1.0, 2.0], [3.0]))
except ValueError:
    print('getRatios called with bad arguments')
