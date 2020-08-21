from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass=ABCMeta):
    def __init__(self):
        self.account_number = None

    @abstractmethod
    def create_account(self):
        return 0

    @abstractmethod
    def validate_account(self):
        return 0

    @abstractmethod
    def withdraw(self, amount):
        return 0

    @abstractmethod
    def deposit(self):
        return 0

    @abstractmethod
    def display_balance(self):
        return 0


class SavingsAccount(Account):
    def __init__(self):
        self.SavingsAccount = {}

    def create_account(self, holder_name, initial_deposit_amount):
        self.account_number = randint(10000, 99999)
        self.SavingsAccount[self.account_number] = [holder_name, initial_deposit_amount]
        print("Congratulations! Account has been created successfully. your account number is ", self.account_number)
        self.display_balance()

    def validate_account(self, account_number, name):
        print(self.SavingsAccount)
        print(self.SavingsAccount.keys())
        if account_number in self.SavingsAccount.keys():
            if self.SavingsAccount[account_number][0] == name:
                self.account_number = account_number
                return True
        return False

    def withdraw(self, amount):
        if amount < self.SavingsAccount[self.account_number][1]:
            self.SavingsAccount[self.account_number][1] -= amount
        else:
            print("Insufficient balance!")
        self.display_balance()

    def deposit(self, amount):
        self.SavingsAccount[self.account_number][1] += amount
        print("Deposit successful")
        self.display_balance()

    def display_balance(self):
        print("Available Bal: ", self.SavingsAccount[self.account_number][1])


sa = SavingsAccount()
while True:
    print("Press 1 to create a new account")
    print("Press 2 to access an existing account")
    print("Press 3 to exit")
    option = int(input())
    if option == 1:
        print("Enter Name: ")
        name = input()
        print("Enter Initial deposit")
        initial_deposit = int(input())
        sa.create_account(name, initial_deposit)
    elif option == 2:
        print("Enter your name")
        name = input()
        print("Enter account number")
        acc_number = int(input())
        if sa.validate_account(acc_number, name):
            while True:
                print("Press 1 to withdraw amount")
                print("Press 2 to deposit amount")
                print("Press 3 to display balance")
                print("Press 4 to go back to previous menu")
                sub_option = int(input())
                if sub_option == 1:
                    print("Enter amount to be withdrawn")
                    amount = int(input())
                    sa.withdraw(amount)
                elif sub_option == 2:
                    print("Enter amount to be deposited")
                    amount = int(input())
                    sa.deposit(amount)
                elif sub_option == 3:
                    sa.display_balance()
                else:
                    break
        else:
            print("Authentication failed!")
    else:
        quit()
