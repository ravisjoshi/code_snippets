student_id = [1, 2, 3, 4, 5]
students = ['Mike', 'Brad', 'Monica', 'Alex', 'Jennifer']
marks = [60.0, 76.4, 79.5, 66.1, 69.9]

for values in zip(student_id, students, marks):
    s_id, s_name, s_marks = values

## If we don't want to use a value we can use _ there

# Example-1: If we need all values but don't know how many will be passed
values = (1, 2, 3, 4, 5)
a, b, *c = values
print('a={}  b={}  c={}'.format(a, b, c))


# Example-2:
values = (1, 2, 3, 4, 5)
a, b, *c, d = values
print('a={}  b={}  c={}  d={}'.format(a, b, c, d))


# Example-3: If we need only some values, and need to ignore rest
values = (1, 2, 3, 4, 5)
a, b, *_ = values
print('a={}  b={}'.format(a, b))


# Example-4: Don't need the value of index
for _ in range(5):
    print('I am printing this line 5 times')
