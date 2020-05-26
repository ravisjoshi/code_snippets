subjects = ['Physics', 'Chemistry', 'Maths', 'Political Science', 'Computer Science']

for index in range(len(subjects)):
    print('{} - {}'.format(index, subjects[index]))

print(25*'-')

# Use enumerate instead
for index, subject in enumerate(subjects):
    print('{} - {}'.format(index, subject))
