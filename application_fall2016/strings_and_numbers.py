import sys
import re

from collections import Counter

INPUT_SET = 'abcdefghijklmnopqrstuvwxyz!"#$%&\\\'()*+,-./:;<=>?@[]^_{|}~'


def main():
    s = bytes(input(), 'utf-8').decode()

    occurrences = Counter(filter(lambda l: l in INPUT_SET, s))
    sorted_occurrences = sorted(occurrences.items(), key=lambda kv: kv[1], reverse=True)

    encodings = {
        symbol[0]: i
        for i, symbol in enumerate(reversed(sorted_occurrences[:10]))
    }

    for symbol in s:
        if symbol in encodings:
            s = s.replace(symbol, str(encodings[symbol]))

    digits = map(int, re.findall(r'\d+', s))
    print(sum(digits))

if __name__ == '__main__':
    sys.exit(main())
