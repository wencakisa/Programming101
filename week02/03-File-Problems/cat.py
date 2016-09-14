import sys
import os


def main():
    files = sys.argv[1:]

    if not files:
        print('Usage: {} <file1> <file2> ...'.format(sys.argv[0]))
        return 1

    for file in files:
        validate_file(file)
        print_file_content(file)


def validate_file(filename: str):
    if not os.access(filename, os.R_OK):
        raise ValueError("I don't have permissions to read this file: {}".format(os.path.relpath(filename)))
    if not os.path.isfile(filename):
        raise ValueError("I can't find this file: {}".format(os.path.relpath(filename)))


def print_file_content(filename: str):
    with open(filename, mode='r', encoding='utf-8') as f:
        print('{}:'.format(os.path.relpath(filename)))
        print(''.join(f.readlines()))
        print()

if __name__ == '__main__':
    sys.exit(main())
