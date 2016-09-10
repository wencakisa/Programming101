import sys
import itertools


def main():
    n = int(input())

    coordinates = [
        tuple(map(int, input().split(' ')))
        for _ in range(n)
    ]

    point1 = coordinates[0]
    point2 = coordinates[1]

    for i in range(2, len(coordinates)):
        point2 = coordinates[i]

        print(point1, point2)

    print(coordinates)


if __name__ == '__main__':
    sys.exit(main())
