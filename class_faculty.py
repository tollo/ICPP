# class_faculty.py
"""Examples of classes, methods and inheritance"""
# Introduction to Computing and Programming using Python


import datetime


class Person(object):
    """Defines a person"""

    def __init__(self, name):
        """Create a person"""
        self.name = name
        try:
            last_blank = name.rindex(' ')
            self.last_name = name[last_blank+1:]
        except:
            self.last_name = name
        self.birthday = None

    def get_name(self):
        """Returns self's full name"""
        return self.name

    def get_last_name(self):
        """Returns self's last name"""
        return self.last_name

    def set_birthday(self, birthdate):
        """Assumes birthdate is of type datetime.date
           Sets self's birthday to birthdate"""
        self.birthday = birthdate

    def get_age(self):
        """Returns self's current age in days"""
        if self.birthday is None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """Returns True if self's name is lexicographically
           less than other's name, and False otherwise"""
        if self.last_name == other.last_name:
            return self.name < other.name
        return self.last_name < other.last_name

    def __str__(self):
        """Returns self's name"""
        return self.name


class MITPerson(Person):
    """Defines a person attending MIT"""

    next_id_num = 0  # Identification Number

    def __init__(self, name):
        """Assigns a number to people attending MIT"""
        Person.__init__(self, name)
        self.id_num = MITPerson.next_id_num
        MITPerson.next_id_num += 1

    def get_id_num(self):
        """Displays the id number of the person"""
        return self.id_num

    def is_student(self):
        """Confirm if the person is a student"""
        return isinstance(self, Student)

    def __lt__(self, other):
        return self.id_num < other.id_num


class Student(MITPerson):
    """Defines a student of MIT"""

    pass


class UG(Student):
    """Defines an undergraduate student"""

    def __init__(self, name, class_year):
        MITPerson.__init__(self, name)
        self.year = class_year

    def get_class(self):
        """Return class year"""
        return self.year


class Grad(Student):
    """Defines a graduate student"""

    pass


class TransferStudent(Student):
    """Defines a transfer student"""

    def __init__(self, name, from_school):
        MITPerson.__init__(self, name)
        self.from_school = from_school

    def get_old_school(self):
        """Show the student's prior school"""
        return self.from_school


class Grades(object):
    """A mapping from students to a list of grades"""

    def __init__(self):
        """Create empty grade book"""
        self.students = []
        self.grades = {}
        self.is_sorted = True

    def add_student(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.get_id_num()] = []
        self.is_sorted = False

    def add_grade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self.grades[student.get_id_num()].append(grade)
        except:
            raise ValueError('Student not in mapping')

    def get_grades(self, student):
        """Return a list of grades for student"""
        try:  # return copy of students grades
            return self.grades[student.get_id_num()][:]
        except:
            raise ValueError('Student not in mapping')

    def get_students(self):
        """Return a list of the students in the grade book"""
        if not self.is_sorted:
            self.students.sort()
            self.is_sorted = True
        for iii in self.students:
            yield iii


def grade_report(course):
    """Assumes course is of type Grades"""
    report = ''
    for iii in course.get_students():
        tot = 0.0
        num_grades = 0
        for jjj in course.get_grades(iii):
            tot += jjj
            num_grades += 1
        try:
            average = tot / num_grades
            report = report + '\n'\
                            + str(iii) + '\'s mean grade is ' + str(average)
        except ZeroDivisionError:
            report = report + '\n'\
                     + str(iii) + ' has no grades'
    return report

UNDERGRADUATE_1 = UG('Jane Doe', 2014)
UNDERGRADUATE_2 = UG('John Doe', 2015)
UNDERGRADUATE_3 = UG('David Henry', 2003)
GRADUATE_1 = Grad('Billy Buckner')
GRADUATE_2 = Grad('Bucky F. Dent')
SIX_HUNDRED = Grades()
SIX_HUNDRED.add_student(UNDERGRADUATE_1)
SIX_HUNDRED.add_student(UNDERGRADUATE_2)
SIX_HUNDRED.add_student(GRADUATE_1)
SIX_HUNDRED.add_student(GRADUATE_2)
for iii in SIX_HUNDRED.get_students():
    SIX_HUNDRED.add_grade(iii, 75)
SIX_HUNDRED.add_grade(GRADUATE_1, 25)
SIX_HUNDRED.add_grade(GRADUATE_2, 100)
SIX_HUNDRED.add_student(UNDERGRADUATE_3)
print(grade_report(SIX_HUNDRED))


# me = Person('Pepito Perez')
# him = Person('John Doe')
# her = Person('Kelly')
# print(him.get_last_name())
# him.set_birthday(datetime.date(1984, 4, 16))
# her.set_birthday(datetime.date(1977, 2, 25))
# print(him.get_name(), 'is', him.get_age(), 'days old')
# pList = [me, him, her]
# for p in pList:
#     print(p)
# pList.sort()
# for p in pList:
#     print(p)
#
# p1 = MITPerson('Sally Smith')
# print(str(p1) + '\'s id number is ' + str(p1.get_id_num()))
#
# p1 = MITPerson('Bob Smith')
# p2 = MITPerson('Joe Brown')
# p3 = MITPerson('Joe Brown')
# p4 = Person('Joe Brown')
#
# p# rint('p1 < p2 =', p1 < p2)
# print('p3 < p2 =', p3 < p2)
# print('p4 < p1 =', p4 < p1)
#
# p5 = Grad('Bill Hunt')
# p6 = UG('Fred Mo', 1973)
# print(p5, 'is a graduate student', type(p5) == Grad)
# print(p5, 'is an undergraduate student is', type(p5) == UG)
#
# print(p5, 'is a student is', p5.is_student())
# print(p6, 'is a student is', p6.is_student())
# print(p3, 'is a student is', p3.is_student())
