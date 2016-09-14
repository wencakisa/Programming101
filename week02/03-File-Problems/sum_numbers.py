import sys

import cat


def main():
    if len(sys.argv) < 2:
        print('Usage: {} <filename>'.format(sys.argv[0]))
        return 1

    filename = sys.argv[1]
    cat.validate_file(filename)

    with open(filename, mode='r', encoding='utf-8') as f:
        numbers_str = f.readline()

        numbers_sum = 0
        for number_str in numbers_str.split(' '):
            try:
                number = int(number_str)
            except TypeError:
                print("I can't parse {} as integer.".format(number_str))
                return 1
            except ValueError:
                continue

            numbers_sum += number

    print(numbers_sum)

if __name__ == '__main__':
    sys.exit(main())
