# https://leetcode.com/problems/simple-bank-system/description

class Bank:

    def __init__(self, balance: List[int]):
        self.accounts = balance
        self.n = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        account1 -= 1
        account2 -= 1
        if account1 >= self.n:
            return False
        if account2 >= self.n:
            return False
        if self.accounts[account1] < money:
            return False
        self.accounts[account1] -= money
        self.accounts[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > self.n:
            return False
        self.accounts[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.n:
            return False
        if self.accounts[account-1] < money:
            return False
        self.accounts[account-1] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
