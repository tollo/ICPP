# Introduction to Computing and Programming using Python


def getGrades(fname):
    try:
        gradesFile = open(fname, 'r')  # open file for reading
    except IOError as err:
        raise ValueError('getGrades could not open ' + fname) from err
    grades = []
    for line in gradesFile:
        try:
            grades.append(float(line))
        except err:
            raise ValueError('Unable to convert line to float') from err
    return grades, err

try:
    grades = getGrades('quiz1grades.txt')
    grades.sort()
    median = grades[len(grades)//2]
    print('Median grade is', median)
except ValueError:
    print('Whoops.')


# raise ValueError('Unable to convert line to float')
# raise ValueError('getGrades could not open ' + fname) as err:
