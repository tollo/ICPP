# Introduction to Computation and Programming using Python
# Remove duplicates from two strings


def removeDups(L1, L2):
    """Assumes that L1 and L2 are lists.
       Removes any element from L1 that also occurs in L2"""
    for e1 in L1[:]:  # [:] makes a copy of the list for loop before mutating
        if e1 in L2:
            L1.remove(e1)
L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
removeDups(L1, L2)
print('L1 = ', L1)
