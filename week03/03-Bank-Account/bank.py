import unittest


class BankAccount:

    def __init__(self, name: str, balance: float, currency: str):
        if balance <= 0:
            raise ValueError('Balance can not be negative.')

        self.name = str(name)
        self.balance = float(balance)
        self.currency = str(currency)
        self.history = ['Account was created']

    def __float__(self):
        self.history.append('__float__ check -> {:.2f}{}'.format(self.balance, self.currency))
        return self.balance

    def __str__(self):
        return 'Bank account for {} with balance of {:.2f}{}'.format(self.name, self.balance, self.currency)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def _is_valid_amount(amount: float):
        """
        Checks if amount is valid
        :param amount: floating point number
        :return: True if it is valid. Otherwise, ValueError.
        """
        if amount <= 0:
            raise ValueError('Amount can not be negative.')

        return True

    def check_balance(self):
        """Checks current balance"""
        self.history.append('Balance check -> {:.2f}{}'.format(self.balance, self.currency))

        return self.balance

    def deposit(self, amount: float) -> bool:
        """
        Deposits money of amount amount
        :param amount: amount to deposit
        :return: True if it was successful. Otherwise, False
        """
        if self._is_valid_amount(amount):
            self.balance += amount
            self.history.append('Deposited {:.2f}{}'.format(amount, self.currency))

            return True

        self.history.append('Deposit for {:.2f}{} failed'.format(amount, self.currency))

        return False

    def withdraw(self, amount: float) -> bool:
        """
        Takes amount money from the account
        :param amount: amount to take
        :return: True if it was successful. Otherwise, False
        """
        if self._is_valid_amount(amount) and self.balance - amount >= 0:
            self.balance -= amount
            self.history.append('{:.2f}{} was withdrawed'.format(amount, self.currency))

            return True

        self.history.append('Withdraw for {:.2f}{} failed'.format(amount, self.currency))

        return False

    def transfer_to(self, other, amount: float) -> bool:
        """
        Transfers amount to account if they both have the same currencies
        :param other: account to transfer to
        :param amount: amount to transfer
        :return: True if it was successful. Otherwise, False
        """
        if self.currency == other.currency and self.balance - amount >= 0:
            self.balance -= amount
            other.balance += amount

            self.history.append('Transfer to {} for {:2f}{}'.format(other.name, amount, self.currency))
            other.history.append('Transfer from {} for {:.2f}{}'.format(self.name, amount, other.currency))

            return True

        self.history.append('Transfer to {} for {:.2f}{} failed'.format(other.name, amount, self.currency))
        other.history.append('Transfer from {} for {:.2f}{} failed'.format(self.name, amount, other.currency))

        return False


class TestBankAccount(unittest.TestCase):

    def test_balance(self):
        self.assertRaises(ValueError, BankAccount, name='test', balance=-50, currency='$')

    def test_deposit(self):
        account = BankAccount(name='test', balance=250, currency='$')

        self.assertIs(account.deposit(230), True)
        self.assertRaises(ValueError, account.deposit, -50)

    def test_withdraw(self):
        account = BankAccount(name='test', balance=250, currency='$')

        self.assertIs(account.withdraw(230), True)
        self.assertIs(account.withdraw(270), False)
        self.assertRaises(ValueError, account.withdraw, -50)

    def test_transfer_to(self):
        account1 = BankAccount(name='test1', balance=250, currency='$')
        account2 = BankAccount(name='test2', balance=700, currency='$')
        account3 = BankAccount(name='test3', balance=1000, currency='€')

        self.assertIs(account1.transfer_to(account2, 200), True)
        self.assertIs(account2.transfer_to(account1, 500), True)
        self.assertIs(account1.transfer_to(account2, 1000), False)
        self.assertIs(account2.transfer_to(account1, 500), False)
        self.assertIs(account1.transfer_to(account3, 100), False)
        self.assertIs(account2.transfer_to(account3, 350), False)


def main():
    rado = BankAccount(name='Rado', balance=2602.76, currency='$')
    ivo = BankAccount(name='Ivo', balance=2312.43, currency='$')
    miki = BankAccount(name='Miki', balance=420, currency='€')

    rado.deposit(240.53)
    rado.check_balance()
    ivo.deposit(135.77)
    ivo.check_balance()
    miki.deposit(356.43)
    miki.check_balance()
    rado.withdraw(1250.49)
    float(rado)
    ivo.withdraw(2000)
    float(ivo)
    miki.withdraw(1002.50)
    float(miki)

    rado.transfer_to(ivo, 1204.53)
    ivo.transfer_to(rado, 420.31)
    miki.transfer_to(rado, 12)
    ivo.transfer_to(miki, 35.12)

    print(rado.history)
    print(ivo.history)
    print(miki.history)

if __name__ == '__main__':
    main()
