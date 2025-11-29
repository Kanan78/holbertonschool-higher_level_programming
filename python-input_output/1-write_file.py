#!/usr/bin/python3
def write_file(filename, text):
    with (filename, 'w') as f:
        return f.write(text)
