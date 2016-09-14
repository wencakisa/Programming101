import sys
import os


def main():
    if len(sys.argv) < 2:
        print('Usage: {} <directory>'.format(sys.argv[0]))
        return 1

    directory = sys.argv[1]

    if not os.access(directory, os.R_OK):
        print("I can't access this directory.")
        return 1
    if not os.path.exists(directory):
        print("Invalid directory.")
        return 1

    size_in_bytes = sum([os.stat(subdir.path).st_size for subdir in os.scandir(directory)])
    size_in_gigabytes = size_in_bytes / 10 ** 9

    print('{} size is: {:.1f}GB'.format(directory, size_in_gigabytes))

if __name__ == '__main__':
    sys.exit(main())
