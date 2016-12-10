# Introduction to Computing and Programming using Python
# Sort Algorithms

import operator


# Selection Sort
def selSort(L):
    """Assumes that L is a list of elements that can be compared using >.
       Sorts L in ascending order"""
    suffixStart = 0
    while suffixStart != len(L):
        # look at each element in suffix
        for i in range(suffixStart, len(L)):
            if L[i] < L[suffixStart]:
                # swap position of elements
                L[suffixStart], L[i] = L[i], L[suffixStart]
        suffixStart += 1


# Merge Sort
def merge(left, right, compare):
    """Assumes left and right are sorted lists and
          compare defines am ordering on the elements.
       Returns a new sorted (by compare) list containing the
          same elements as (left + right) would contain."""

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
            result.append(right[j])
            j += 1
    return result


def mergeSort(L, compare=operator.lt):
    """Assumes L is a list, compare defines an ordering
          on elements of L
       Returns a new sorted list containing the same elements as L"""
    if len(L) < 2:
        # print('in mergeSort: length of L is <2')
        return L[:]
    else:
        middle = len(L)//2
        # print('ms middle', middle)
        left = mergeSort(L[:middle], compare)
        # print('ms left', left)
        right = mergeSort(L[middle:], compare)
        # print('ms right', right)
        return merge(left, right, compare)


def lastNameFirstName(name1, name2):
    import string
    name1 = string.split(name1, ' ')
    # print('lnfn name1', name1)
    name2 = string.split(name2, ' ')
    # print('lnfn name2', name2)
    if name1[1] != name2[1]:
        return name1[1] < name2[1]
    else:  # last names the same, sort by first name
        return name1[0] < name2[0]


def firstNameLastName(name1, name2):
    import string
    name1 = string.split(name1, ' ')
    name2 = string.split(name2, ' ')
    if name1[0] != name2[0]:
        return name1[0] < name2[0]
    else:  # last names the same, sort by first name
        return name1[1] < name2[1]

L = ['Chris Terman', 'Tom Brady', 'Eric Grimson', 'Giselle Bundchen']
newL = mergeSort(L, lastNameFirstName)
print('Sorted by last name', newL)
newL = mergeSort(L, firstNameLastName)
print('Sorted by first name', newL)
