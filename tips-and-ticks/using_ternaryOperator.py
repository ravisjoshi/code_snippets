num = 3

if num % 2 == 0:
    print('Even')
else:
    print('Odd')

# Using ternary operator
result = 'Even' if num % 2 == 0 else 'Odd'
print(result)

# OR
result = 'Even' if num % 2 == 0 else print('Odd')
