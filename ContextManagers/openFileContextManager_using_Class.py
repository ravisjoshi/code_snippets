"""
In this section we will write a file open context manager using class:
    file_handle = open(filename, mode)
    .
    .
    file_handle.close()
"""

class file_open:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    # Will execute while entering with block
    def __enter__(self):
        self.fh = open(self.filename, self.mode)
        return self.fh

    # Will execute while exiting with block
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.fh.close()


with file_open('sample.txt', 'w') as f:
    f.write('This is sample file content!')

# Check if file is closed outside with block or not
print(f.closed)

