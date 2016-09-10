def is_number_balanced(n: int) -> bool:
    n_list = list(map(int, str(n)))
    n_list_len = len(n_list)

    if n_list_len % 2 != 0:
        del n_list[n_list_len // 2]

    n_list_half_len = len(n_list) // 2

    return sum(n_list[: n_list_half_len]) == sum(n_list[n_list_half_len:])


def is_increasing(seq: list) -> bool:
    return sorted(seq) == seq and len(set(seq)) == len(seq)


def is_decreasing(seq: list) -> bool:
    return sorted(seq, reverse=True) == seq and len(set(seq)) == len(seq)


def get_largest_palindrome(n: int) -> int:
    for i in range(n - 1, 0, -1):
        if str(i) == str(i)[::-1]:
            return i


def prime_numbers(n: int) -> list:
    return [i for i in range(2, n + 1) if all(i % x for x in range(2, i))]


def is_anagram(a: str, b: str) -> bool:
    return sorted(a.lower()) == sorted(b.lower())


def birthday_ranges(birthdays: list, ranges: list) -> list:
    result = []

    for start, end in ranges:
        count = 0

        for birthday in birthdays:
            if birthday in range(start, end + 1):
                count += 1

        result.append(count)

    return result


def sum_matrix(m: list) -> int:
    return sum(sum(row) for row in m)


def matrix_bombing_plan(m: list) -> dict:
    result = {}

    for row_index, row in enumerate(m):
        for row_element_index, row_element in enumerate(row):
            key = row_index, row_element_index
            bombing_site = row_element

            result[key] = sum_matrix(
                [
                    [m[x][y] - bombing_site if m[x][y] - bombing_site >= 0 else 0 for y in range(len(row))]
                    for x in range(len(m))
                ]
            )

    return result


def is_transversal(transversal: list, family: list) -> bool:
    return all(set(transversal) & row for row in map(set, family))
