
class BankAccount():
    _num_accounts = 0
    
    def __init__(self):
        self._num_accounts += 1
        self._balance = 0
        
    @classmethod
    def num_account(cls):
        return cls._num_accounts
    
    @staticmethod
    def print_bank_account(account):
        print(f'Your balance: {account.balance}')
        
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, value):
        if value > 0:
            self._balance += value
        else:
            raise ValueError('Для пополнения недостаточно средств!')
    
    @staticmethod    
    def log(func):
        def fun(self, *args):
            print(f'Balance: {self.balance}')
            func(self, *args)
            print(f'Balance: {self.balance}')
        return fun
    
    @log
    def withdraw(self,value):
        if self._balance >= value:
            self._balance -= value
        else:
            raise ValueError('Недостаточно денег на балансе!')
    
     
a = BankAccount()

a.deposit(100)
print(a.withdraw(20))
print(a.balance)

