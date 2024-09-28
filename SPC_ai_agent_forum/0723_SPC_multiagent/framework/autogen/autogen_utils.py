import os
import sys
from contextlib import redirect_stdout
from contextlib import contextmanager

class Tee:
    def __init__(self, *files):
        self.files = files
        self.open_files = list(files)  # Keep track of open files

    def write(self, obj):
        for f in self.open_files:
            f.write(obj)
            f.flush()  # Ensure real-time writing

    def flush(self):
        for f in self.open_files:
            f.flush()

    def close(self):
        for f in self.open_files:
            if f != sys.stdout and not f.closed:
                f.close()
        self.open_files = []  # Clear the list of open files

@contextmanager
def redirect_stdout_to_file_and_terminal(file):
    original_stdout = sys.stdout
    tee = Tee(sys.stdout, file)
    sys.stdout = tee
    try:
        yield
    finally:
        tee.close()  # Close the Tee object
        sys.stdout = original_stdout