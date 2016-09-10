import sys
import itertools


def main():
    user_input = 'H, T, H, T, T, H, H'
    splitted_user_input = user_input.split(', ')

    max_consecutive_throws = max(len(list(grouper)) for header, grouper in itertools.groupby(splitted_user_input))

    result = set(
        header
        for header, grouper in itertools.groupby(splitted_user_input)
        if len(list(grouper)) == max_consecutive_throws
    )

    print('{} wins!'.format(result.pop()) if len(result) == 1 else 'Draw!')

if __name__ == '__main__':
    sys.exit(main())
