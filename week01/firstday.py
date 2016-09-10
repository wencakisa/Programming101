def sum_of_digits(n: int) -> int:
    n_str = str(n)[1:] if str(n).startswith('-') else str(n)

    return sum(digit for digit in map(int, list(n_str)))


def number_to_list(n: int) -> list:
    return list(map(int, str(n)))


def list_to_number(digits: list) -> int:
    return int(''.join(map(str, digits)))


def fact_digits(n: int) -> int:
    result = []

    for digit in map(int, str(n)):
        # from math import factorial
        # result.append(factorial(digit))

        fact = 1
        for i in range(1, digit + 1):
            fact *= i

        result.append(fact)

    return sum(result)


def fibonacci(n: int) -> list:
    result = []
    a, b = 0, 1

    for i in range(n):
        a, b = b, a + b
        result.append(a)

    return result


def fib_number(n: int) -> int:
    return int(''.join(map(str, fibonacci(n))))


def palindrome(n: object) -> bool:
    return str(n) == str(n)[::-1]


def count_vowels(string: str) -> int:
    return len([l for l in string if l in 'aeiouy'])


def count_consonants(string: str) -> int:
    return len([l for l in string if l in 'bcdfghjklmnpqrstvwxz'])


def char_histogram(string: str) -> dict:
    # from collections import Counter
    # return Counter(string)

    result = {}

    for letter in string:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 0

    return result
