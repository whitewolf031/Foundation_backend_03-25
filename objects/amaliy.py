class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self):
        self.total_balance = self.__balance + 100_000
        return f"Siz balansingizga 100 000 ming so'm qo'shdingiz",

    def withdraw(self):
        return f"Sizning jami balancingiz {self.total_balance}"

obj = BankAccount(1_000_000)
print(obj.deposit())
print(obj.withdraw())