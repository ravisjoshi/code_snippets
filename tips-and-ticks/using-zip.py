student_id = [1, 2, 3, 4, 5]
students = ['Mike', 'Brad', 'Monica', 'Alex', 'Jennifer']
marks = [60.0, 76.4, 79.5, 66.1, 69.9]

for s_id, name, marks in zip(student_id, students, marks):
    print('{}: {} {}'.format(s_id, name, marks))


## If you have some short lists - where data is missing
from itertools import zip_longest

student_id = [1, 2, 3, 4, 5, 6, 7]
students = ['Mike', 'Brad', 'Monica', 'Alex', 'Jennifer', 'Carl', 'Shawn']
marks = [60.0, 76.4, 79.5, 66.1, 69.9]

for s_id, name, marks in zip_longest(student_id, students, marks, fillvalue='New student'):
    print('{:2}:  {:10} - {}'.format(s_id, name, marks))
