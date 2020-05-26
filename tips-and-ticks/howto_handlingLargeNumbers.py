num1 = 1000000000
num2 = 100000000
print('Input with hard readability - output: {}'.format(num1+num2))

# We can add underscore for better readability
num1 = 1_000_000_000
num2 = 100_000_000
print('Input with easy readability - output: {}'.format(num1+num2))

# OR We can add separators in output too
num1 = 1_00_00_00_000
num2 = 10_00_00_000
print('Input with easy readability and output seperators: {:,}'.format(num1+num2))
