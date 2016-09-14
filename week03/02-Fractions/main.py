import sys


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __eq__(self, other):
        return self.numerator / self.denominator == other.numerator / other.denominator

    def __str__(self):
        return '{} / {}'.format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()


def main():
    a = Fraction(1, 2)
    b = Fraction(2, 4)

    print(a == b)
    print(a + b)


if __name__ == '__main__':
    sys.exit(main())
