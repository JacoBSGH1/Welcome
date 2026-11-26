import datetime

import pandas as pd
import os

rates_file = os.path.join('data', 'rates.csv')
df = pd.read_csv(rates_file)
df_cur = df.set_index('Currency')
rates = df_cur['Value'].to_dict()

class Customer:
    last_id = 0

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return f"C[{self.id}, {self.first_name}, {self.last_name}]"

class Account:
    last_id = 1000
    yearly_interest_rate = 0.02

    def __init__(self, customer, currency='USD'):
        self.customer = customer
        self.currency = currency
        Account.last_id += 1
        self.id = Account.last_id
        self.__balance = 0
        self.transactions = []

    def get_balance(self):
        return self.__balance

    def deposit(self, amount: int, d_currency, transaction="Deposit"):
        if amount <= 0:
            raise InvalidAmountException(f"Invalid value {amount}")
        if d_currency not in rates:
            raise NonAvailableCurrencyException(f"Currency {d_currency} is not available for transactions")
        if d_currency != self.currency:
            amount = amount * rates[self.currency]/rates[d_currency]
        self.__balance += round(amount,2)
        self.transactions.append(AccountTransaction(transaction,amount))

    def withdraw(self, amount: int):
        if amount <= 0:
            raise InvalidAmountException(f"Invalid value {amount}")
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            raise InsufficientFundsException(f"Insufficient funds requested/available {amount}/{self.__balance}", amount, self.__balance)

    def apply_interest(self, yearly_interest_rate):
        self.yearly_interest_rate = yearly_interest_rate
        daily_rate = yearly_interest_rate/365
        interest = round(self.__balance * daily_rate,2)
        self.__balance += interest
        return interest

    def transaction_report(self, account):
        pass

    def __repr__(self):
        return f"A[{self.id}, {self.customer.last_name}, {self.__balance} {self.currency}]"

class AccountTransaction:
    last_id = 0
    def __init__(self, transaction, amount):
        self.timestamp = datetime.datetime.now()
        self.transaction = transaction
        AccountTransaction.last_id += 1
        self.transaction_id = AccountTransaction.last_id
        self.amount = amount
    def __repr__(self):
        time_format = self.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        return f"Transaction no.: {self.transaction_id}, Time: {time_format}, Amount:{self.amount:.2f}"

class Bank:
    def __init__(self, name):
        self.name = name
        self.cust_list = []
        self.acc_list = []
        self.selected_account = None

    def create_customer(self, first_name, last_name):
        customer = Customer(first_name, last_name)
        self.cust_list.append(customer)
        return customer

    def create_account(self, customer, currency = 'USD'):
        account = Account(customer, currency)
        self.acc_list.append(account)
        return account

    def account_select(self, account_id):
        for account in self.acc_list:
            if account.id == account_id:
                self.selected_account = account
                return account
        raise InvalidAccountException(f"Account with this id does not exist: {account_id}")

    def transfer_money(self, from_account_id, to_account_id, amount):
        if amount <= 0:
            raise InvalidAmountException(f"Transfer amount must be positive {amount}")
        if from_account_id == to_account_id:
            raise InvalidAccountException(f"Cannot transfer money to the same account")

        from_account_id = self.account_select(from_account_id)
        to_account_id = self.account_select(to_account_id)

        if from_account_id.get_balance() < amount:
            raise InsufficientFundsException(f"Not enough money to make a transfer: {amount/from_account_id.balance}", amount, from_account_id.balance)

        from_account_id.withdraw(amount)
        to_account_id.deposit(amount, d_currency=from_account_id.currency)

    def run_daily_interest_updater(self):
        for account in self.acc_list:
            account.apply_interest(Account.yearly_interest_rate)

    def __repr__(self):
        return f'{self.name} bank[\n{self.cust_list}\n{self.acc_list}]'


class BankException(Exception):
    pass

class InvalidAmountException(BankException):
    pass

class InsufficientFundsException(BankException):
    def __init__(self, message, amount_req, amount_avl):
        super().__init__(message)
        self.amount_req = amount_req
        self.amount_avl = amount_avl

class InvalidAccountException(BankException):
    pass

class NonAvailableCurrencyException(BankException):
    pass