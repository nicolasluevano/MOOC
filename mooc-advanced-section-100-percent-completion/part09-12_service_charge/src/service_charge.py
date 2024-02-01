# WRITE YOUR SOLUTION HERE:

class BankAccount:
    def __init__(self, name: str, account_num: int, balance: float):
        self.__name = name
        self.__account_num = account_num
        self.__balance = float(balance)

    def deposit(self, amount: float):
        self.__balance += amount
        self.__service_charge()

    def withdraw(self, amount: float):
        self.__balance -= amount
        self.__service_charge()

    @property
    def balance(self):
        return self.__balance

    # decreases the balance by one percent
    # call this method when deposit or withdraw is called
    # service charge calculated when deposit or withdraw is completed
    def __service_charge(self):
        fee = (self.__balance * 1) / 100
        self.__balance -= fee


if __name__ == "__main__":

    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)

