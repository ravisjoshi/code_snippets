
fh = open('sample.txt', 'r')
file_data = fh.read()
print(file_data)
fh.close()

# Adding a separator between 2 method outputs
print(25*'-')

# Use context manager 'with' to open files - this way we don't have to remember to close file handle
with open('sample.txt', 'r') as file_write:
    file_content = file_write.read()
    print(file_content)
