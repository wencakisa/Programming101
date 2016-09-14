import sys
import os
from random import randint

import cat


def main():
    if len(sys.argv) < 3:
        print('Usage: {} <numbers_file> <random_max>'.format(sys.argv[0]))
        return 1

    filename = sys.argv[1]

    if not os.access(filename, os.W_OK):
        raise ValueError("I don't have permissions to write in this file: {}".format(os.path.relpath(filename)))
    if not os.path.isfile(filename):
        raise ValueError("I can't find this file: {}".format(os.path.relpath(filename)))

    random_max = sys.argv[2]

    try:
        random_max = int(random_max)
    except TypeError:
        print('random_max parameter must be integer.')
        return 1

    if random_max <= 0:
        raise ValueError('Negative numbers are not supported: {}'.format(random_max))

    with open(filename, mode='w', encoding='utf-8') as f:
        for _ in range(random_max):
            f.write(str(randint(1, 1000)) + ' ')

    cat.print_file_content(filename)


if __name__ == '__main__':
    sys.exit(main())
