class Account:
    def open_acc(self):
        print('account created')

    def deposit(self):
        print('amount deposited')

    def withdraw(self):
        print('amount withdrawl')

    def get_bal(self):
        print('bal is -ve.please deposit more')
        
    def close_acc(self):
        print('account closed')

a1=Account()
a2=Account()

a1.open_acc()
a1.deposit()
a1.withdraw()
a1.get_bal()
a1.close_acc()