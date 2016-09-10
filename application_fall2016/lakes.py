import sys
import itertools

FULL_SQUARE_CAPACITY = 1000


def main():
    user_input = 'ddhhuu'

    result = 0
    for direction, grouper in itertools.groupby(user_input):
        grouper = list(grouper)

        if direction == 'd' or direction == 'u':
            result += FULL_SQUARE_CAPACITY * 2 * (len(grouper) - 1)
        else:
            result += FULL_SQUARE_CAPACITY * 2 * (len(grouper))

        print(result)
        print('*' * 100)

    print(result)

if __name__ == '__main__':
    sys.exit(main())
