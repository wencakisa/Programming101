from typing import List


class Bill:
    def __init__(self, amount: int):
        self.amount = amount

    def __str__(self):
        return 'A {}$ {}'.format(self.amount, self.__class__.__name__)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        if self.amount < 0:
            raise ValueError("Amount can't be negative.")
        if int(self.amount) != self.amount:
            raise TypeError("Amount should be an integer.")

        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __hash__(self):
        return hash(self.amount)


class BillBatch:
    def __init__(self, bills: List[Bill]):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def __getitem__(self, item):
        return self.bills[item]

    def total(self):
        return sum(bill.amount for bill in self.bills)


class CashDesk:
    def __init__(self):
        self.bills = []

    def take_money(self, money):
        self.bills.extend(money) if isinstance(money, BillBatch) else self.bills.append(money)

    def total(self):
        return sum(bill.amount for bill in self.bills)

    def inspect(self):
        print('\n'.join([
            'We have a total of {}$ in the desk'.format(self.total()),
            'We have the following count of bills, sorted in ascending order:',
            '\n'.join([
                '{} - {}'.format(bill, self.bills.count(bill)) for bill in sorted(set(self.bills))
            ])
        ]))


def main():
    values = [10, 20, 50, 100, 100, 100]
    bills = [Bill(value) for value in values]

    batch = BillBatch(bills)

    desk = CashDesk()

    desk.take_money(batch)
    desk.take_money(Bill(10))

    desk.inspect()

if __name__ == '__main__':
    main()