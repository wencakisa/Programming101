import itertools
import re

TELEPHONE_KEYBOARD = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: [' ']
}


def main():
    print(message_to_numbers('Ivo e Panda'))


def count_words(arr: list) -> dict:
    # from collections import Counter
    # return Counter(arr)

    result = {}

    for word in arr:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result


def nan_expand(times: int):
    return 'Not a ' * times + 'Nan'


def iterations_of_nan_expand(expanded: str) -> int:
    if 'Nan' not in expanded:
        return False

    return expanded.count('Not a')


def group(arr: list) -> list:
    return [list(g) for _, g in itertools.groupby(arr)]


def max_consecutive(items: list) -> int:
    return max(len(list(g)) for _, g in itertools.groupby(items))


def gas_stations(distance: int, tank_size: int, stations: list) -> list:
    result = []

    # TODO: implement.

    return result


def sum_of_numbers(st: str) -> int:
    return sum(map(int, re.findall('\d+', st)))


def numbers_to_message(pressed_sequence: list) -> str:
    pass


def message_to_numbers(message: str) -> list:
    # TODO: Add functionality for -1 (sequence break)

    result = []

    for letter in message:
        if letter.isupper():
            result.append(1)
            letter = letter.lower()

        for number, letters in TELEPHONE_KEYBOARD.items():
            if letter in letters:
                for i in range(letters.index(letter) + 1):
                    result.append(number)

    return result


if __name__ == '__main__':
    main()
