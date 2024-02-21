class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount != abs(amount): #zero
            raise ValueError("Cannot deposit zero or negative funds")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount != abs(amount):
            raise ValueError("Cannot withdraw zero or negative funds")
        elif amount > self.__balance:
            raise ValueError("Insufficient funds")
        else:
            self.__balance -= amount
        
