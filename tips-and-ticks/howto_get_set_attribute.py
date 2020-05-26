
class student:
    pass

s_obj = student()

student_info = {'first_name': 'Robert', 'last_name': 'Langdon'}

for key, value in student_info.items():
    setattr(s_obj, key, value)

print(s_obj.first_name)
print(s_obj.last_name)

print(25*'-')

for key in student_info:
    print(getattr(s_obj, key))
